import unittest
from qamodel import ScienceChatBot
from sentence_transformers import SentenceTransformer


class ScienceChatBotTest(unittest.TestCase):
    def setUp(self):
        self.chatbot = ScienceChatBot()
        self.question = "Bones, cartilage, and ligaments make up what anatomical system?"
        self.keywords = ["bones", "cartilage"]

    def test_extract_keywords(self):
        keywords = self.chatbot.extract_keywords(self.question)
        keywords = [str(keyword).lower() for keyword in keywords]
        self.assertIsInstance(keywords, list)
        self.assertGreater(len(keywords), 0)
        self.assertIn("bones", keywords)
        self.assertIn("cartilage", keywords)

    def test_fetch_wikipedia_articles(self):
        articles = self.chatbot.fetch_wikipedia_articles(self.keywords)
        self.assertIsInstance(articles, list)
        self.assertGreater(len(articles), 0)

    def test_filter_and_combine_articles(self):
        keywords = self.chatbot.extract_keywords(self.question)
        articles = self.chatbot.fetch_wikipedia_articles(keywords)
        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        context = self.chatbot.filter_and_combine_articles(self.question, articles, model)
        self.assertIsInstance(context, str)
        self.assertGreater(len(context), 0)

    def test_predict_answer(self):
        questions = [self.question]
        answers = self.chatbot.predict_answer(questions)
        self.assertIsInstance(answers, list)
        self.assertGreater(len(answers), 0)
        self.assertNotEqual(answers[0], "I could not find an answer to that!")


if __name__ == '__main__':
    unittest.main()
