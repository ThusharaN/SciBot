# A ChatBot for Science!

## <u>About the project</u>
The intuition behind this project was to build a chatbot that mimics the Retriever-Generator mode of Question-Answering (QA) with a some nuances. Our QA pipeline, thus, unfolds in three key stages:
- [YAKE](https://liaad.github.io/yake/) does Keyword Extraction 🔑
    - Leveraging YAKE, our Keyword Extractor, we unveil essential keywords from questions. 
    - Configurations, like the number of keywords and maximum words per keyword, shape the process.
- Get more Context! 📖
    - Unearthing answers requires context. We adopt a two-pronged strategy.
    - We pinpoint Wikipedia articles related to selected keywords, essentially turning Wikipedia into our Retriever-Generator knowledge base.
    - A straightforward similarity mechanism filters and merges relevant articles to craft the perfect context for our questions.
- [RoBERTa](https://huggingface.co/deepset/roberta-base-squad2) finds the Answer 🤖
    - Armed with the question and context, RoBERTa steps in to predict the answer.


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

### Using Swagger
Run the start script to open Swagger UI and interact with the execute API endpoint:
```sh
./start.sh
```
A demo showcasing the Swagger interface is presented below.

### Using our own Custome UI!
As a full-stack engineer, I couldn't help but include a basic UI built using [Flask](https://flask.palletsprojects.com/en/3.0.x/) for richer experience. Follow these steps to explore:
Set Flask to the app file and development environment:
```sh
export FLASK_APP=chatbot
export FLASK_ENV=development
```
Then, launch the Flask app:
```sh
flask run
```

A demo featuring the Custom UI is shown for your convenience.
