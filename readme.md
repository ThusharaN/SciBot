# A ChatBot for Science!

![Python](https://img.shields.io/badge/python-3.9.12-brightgreen.svg)
[![Flask](https://img.shields.io/badge/flask-2.3.3-brightgreen.svg)](https://pypi.org/project/Flask/)
[![Wikipedia API](https://img.shields.io/badge/wikipedia--api-0.6.0-brightgreen.svg)](https://pypi.org/project/Wikipedia-API/)
[![Sentence Transformers](https://img.shields.io/badge/sentence--transformers-2.2.2-brightgreen.svg)](https://pypi.org/project/sentence-transformers/) 
[![Transformers](https://img.shields.io/badge/transformers-4.36.2-brightgreen.svg)](https://pypi.org/project/transformers/)
[![YAKE](https://img.shields.io/badge/yake-0.4.8-brightgreen.svg)](https://pypi.org/project/yake/)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/ThusharaN/SciBot.svg?color=blue)](https://github.com/ThusharaN/SciBot/pulls)


## <u>About the project</u>
The intuition behind this project was to build a chatbot that mimics a Retriever-Generator approach for Open-Domain Question-Answering (QA). Our QA pipeline, thus, unfolds in three key stages:
### 1. [YAKE](https://liaad.github.io/yake/) does Keyword Extraction 🔑
- Leveraging YAKE, our Keyword Extractor, we identify important keywords from the questions. 
- Configurations, like the number of keywords and maximum words per keyword, shape the process.
### 2. Get more Context! 📖
- Unearthing answers requires context. We adopt a two-pronged strategy.
- We pinpoint Wikipedia articles related to selected keywords, essentially turning Wikipedia into our knowledge base i.e., our domain.
- A straightforward similarity mechanism filters and merges relevant articles to craft a relevant context for our questions.
### 3. [RoBERTa](https://huggingface.co/deepset/roberta-base-squad2) finds the Answer 🤖
- Armed with the question and context, RoBERTa steps in to predict the answer.

### I have created a short video explaining the approach to building this project and a demo of the ChatBot. You can find it here: [SciBot Demo](https://drive.google.com/file/d/1-tqXBtFVTgST2XpsJeykI5j08F3mOSv_/view?usp=drive_link)

## <u>Core Functions</u>
### `main.py`
- Callback function called on each execution pass.
- Initializes ScienceChatBot and predicts answers for user questions using the `predict_answer` method.
- Returns the response in the form of SimpleText.
- Answers are formatted as a list of strings, where each string is a concatenation of the question and its corresponding answer separated by a colon.

### `qamodel.py`
- Defines and initializes the `ScienceChatBot` class with configuration data from a YAML file (using `config.yaml`).
- Implements functions for keyword extraction, fetching Wikipedia articles, filtering and combining article content, and predicting answers based on user questions.
> **_NOTE:_** Detailed documentation about the individual functions can be found within the `qamodel.py` file.

### `chatbot.py`
- Renders the HTML template for the chatbot interface.
- Processes user input, gets the predicted answers, and returns the responses in JSON format.

### `index.html`
- HTML template for the custom SciBot UI.
- Uses Internal styling to render the interface and AJAX server to send user input to and receive chatbot output from the backend

### `config.yaml`
- Specifies configuration settings for SciBot.

### `qatest.py`
- Contains unit test cases to test the basic functionalities of SciBot.


## <u>How to run?</u>
Before diving into the project, let's set up the groundwork. First, activate the project's virtual environment using poetry:
```sh
poetry shell
```

Afterward, install the essential dependencies:
```sh
poetry install
```
With these steps complete, there are two ways to run the project.

### Swagger UI
Run the start script to open Swagger UI and interact with the execute API endpoint:
```sh
./start.sh
```
The Swagger endpoint can be found at `http://0.0.0.0:5500/swagger-ui/`

Here is a demo showing the Swagger interface:
![eac7d564-8b61-4f1a-8b2a-d71c5059a536](https://github.com/ThusharaN/ScienceChatBot/assets/85170859/1552c89c-dbab-459e-8192-89da093a8b19)
_(The gif may render slower than the actual speed!)_

### Our own Custom UI!
As a full-stack engineer, I couldn't help but include a basic UI built using [Flask](https://flask.palletsprojects.com/en/3.0.x/) for a richer experience. I have gone with a toned down version of [OpenFabric AI's](https://openfabric.ai/) theme of blues and pinks for this custom UI. Follow these steps to interact with the SciBot UI:

Set Flask to the app file and development environment:
```sh
export FLASK_APP=chatbot
export FLASK_ENV=development
```
Then, launch the Flask app:
```sh
flask run
```
The app will be up and running on the server `http://127.0.0.1:5000/`

A demo featuring the Custom UI:
![6d57872a-19fb-4216-8e22-cf2fb46a7a3c](https://github.com/ThusharaN/SciBot/assets/85170859/57c0802b-03f9-4e06-9abd-e691d39997e8)
_(The gif may render slower than the actual speed!)_


## <u>Evaluating on SciQ</u>
The chatbot was tasked with answering some of the questions from the [SciQ dataset](https://huggingface.co/datasets/sciq). 
There are 2 aspects that can be evaluated from the responses: 
- Context Quality Assessment: Examining the effectiveness of the chatbot in retrieving relevant context following keyword extraction, and
- Model Accuracy Assessment: Evaluating the precision of the model in predicting accurate answers based on the retrieved context.
> **_NOTE:_** Since SciBot itself fetches the context for the question through keyword extraction, the context supplied with the SciQ dataset is **NOT** used.

| **Question**                                                                                  |**Actual Answer**|**Predicted Answer**      |
| ----------------------------------------------------------------------------------------------| ----------------|--------------------------|
| Through which process are plants able to make their own food?                                 | photosynthesis  | photosynthesis           |
| Each specific polypeptide has a unique linear sequence of which acids?                        | amino           | amino acids              |
| What is the most common type of anemia?                                                       | iron-def        | Iron-deficiency anemia   |
| What  is the process by which the nucleus of a eukaryotic cell divides?                       | mitosis         | mitosis                  |
| What mineral is used in jewelry because of its striking greenish-blue color?                  | turquoise       | malachite                |
| What are hydrocarbons most important use?                                                     | fuel            | fuels and chemicals      |
| When a hypothesis is repeatedly confirmed, what can it then become?                           | theory          | part of a theory         |
| The effect of acetylcholine in heart muscle is inhibitory rather than what?                   | excitatory      | excitatory               |
| What is process of producing eggs in the ovary called?                                        | oogenesis       | meiosis                  |
| A phase diagram plots pressure and what else?                                                 | temperature     | temperature              |
| Energy resources can be put into two categories — renewable or?                               | nonrenewable    | non-renewable            |
| Who proposed the theory of evolution by natural selection?                                    | darwin          | Charles Darwin & Alfred Russel Wallace |
| What is the term for the secretion of saliva?                                                 | salivation      | spit                     |
| Caffeine and alcohol are two examples of what type of drug?                                   | psychoactive    | stimulant                |
| Sometimes referred to as air, what do we call the mixture of gases that surrounds the planet? | atmosphere      | The atmosphere of Earth  |
| Who was the first person known to use a telescope to study the sky?                           | galileo         | Galileo Galilei          |

## <u>Unit Tests</u>
The unit test cases can be excuted by running the following command:
```sh
python -m unittest qatest.py
```
The latest code has been tested against these test cases locally. Below is a screenshot showing the test results:
<img width="796" alt="Screenshot 2024-01-15 at 5 20 57 PM" src="https://github.com/ThusharaN/SciBot/assets/85170859/24dac1bb-98a8-4fca-8507-073cb0d97de3">
