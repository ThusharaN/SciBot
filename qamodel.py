import wikipediaapi
import yake
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import yaml


class ScienceChatBot:
    def __init__(self):
        with open("config.yaml", "r") as yamlfile:
            self.data = yaml.load(yamlfile, Loader=yaml.FullLoader)

        model_name = self.data['model_name']
        self.oracle = pipeline(model=model_name)

    def extract_keywords(self, question):
        """Extract relevant keywords from the question using YAKE (Yet Another Key Extractor) model
        Args:
            question (str): a single question
        Returns:
            list: a list of keywords
        """

        custom_kw_extractor = yake.KeywordExtractor(lan=self.data['language'], n=self.data['max_ngram_size'],
                                                    dedupLim=self.data['deduplication_threshold'], dedupFunc=self.data['deduplication_algo'],
                                                    windowsSize=self.data['windowSize'], top=self.data['numOfKeywords'], features=None)
        keywords = custom_kw_extractor.extract_keywords(question)
        return [kw[0] for kw in keywords]

    def fetch_wikipedia_articles(self, keywords):
        """Identify wikipedia articles for the all the keywords in the question
        Args:
            keywords (list): a list of keywords
        Returns:
            list: a list of wikipedia articles
        """

        user_agent = self.data['user_agent']
        wiki_wiki = wikipediaapi.Wikipedia(
            user_agent=user_agent, language="en", extract_format=wikipediaapi.ExtractFormat.WIKI)
        articles = []
        for keyword in keywords:
            # Fetch Wikipedia articles for each keyword
            page_py = wiki_wiki.page(keyword)
            # Check if the page exists
            if page_py.exists():
                # Store the title and content of the article
                articles.append({
                    'title': page_py.title,
                    'content': page_py.text
                })
        return articles

    def filter_and_combine_articles(self, question, articles, model, threshold=0.5):
        """Filter only the relevant context from the wikipedia articles using a SentenceTransformer
        Args:
            question (str): a single question
            articles (list): a list of wikipedia articles
            model (SentenceTransformer): a model to convert the question & articles into their respective embeddings
            threshold (int): a threshold value to filter out not-so-relevant wikipedia articles
        Returns:
            str: final context for the question
        """

        # Encode the question and article content
        question_embedding = model.encode(
            question, convert_to_tensor=True, show_progress_bar=False)
        article_embeddings = model.encode(
            [article['content'] for article in articles], convert_to_tensor=True, show_progress_bar=False)

        # Calculate cosine similarities between the question and articles
        semantic_similarities = util.pytorch_cos_sim(
            question_embedding, article_embeddings)[0].tolist()

        # Shortlist articles above the threshold
        shortlisted_articles = [article for article, score in zip(
            articles, semantic_similarities) if score >= threshold]

        # Combine the contents of the shortlisted articles
        combined_content = ' '.join([article['content']
                                    for article in shortlisted_articles])

        return combined_content

    def predict_answer(self, questions):
        """Predict the answer to the questions asked by the user
        Args:
            questions (list): list of questions passed by the user
        Returns:
            list: list of answers for the corresponding questions
        """

        answers = []
        for question in questions:
            # Extracting keywords from the question
            keywords = self.extract_keywords(question)

            # Identifying available context for the keywords identified
            articles = self.fetch_wikipedia_articles(keywords)

            # Use a pre-trained SentenceTransformer model for semantic similarity
            # Identify relevant context for the question
            context_model = SentenceTransformer(
                self.data['sentence_transformer'])
            context = self.filter_and_combine_articles(
                question, articles, context_model)

            # Answering the question
            prediction = "I could not find an answer to that!"
            if context != "":
                prediction = self.oracle(
                    question=question, context=context)['answer']
            answers.append(prediction)

        return answers
