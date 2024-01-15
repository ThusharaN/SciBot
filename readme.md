# A ChatBot for Science!

## <u>About the project</u>
The intuition behind this project was to build a chatbot that mimics a Retriever-Generator approach for Open-Domain Question-Answering (QA). Our QA pipeline, thus, unfolds in three key stages:
### [YAKE](https://liaad.github.io/yake/) does Keyword Extraction 🔑
- Leveraging YAKE, our Keyword Extractor, we unveil essential keywords from questions. 
- Configurations, like the number of keywords and maximum words per keyword, shape the process.
### Get more Context! 📖
- Unearthing answers requires context. We adopt a two-pronged strategy.
- We pinpoint Wikipedia articles related to selected keywords, essentially turning Wikipedia into our Retriever-Generator knowledge base.
- A straightforward similarity mechanism filters and merges relevant articles to craft the perfect context for our questions.
### [RoBERTa](https://huggingface.co/deepset/roberta-base-squad2) finds the Answer 🤖
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
The Swagger endpoint can be found at `http://0.0.0.0:5500/swagger-ui/`

Here is a demo showing the Swagger interface:
![eac7d564-8b61-4f1a-8b2a-d71c5059a536](https://github.com/ThusharaN/ScienceChatBot/assets/85170859/1552c89c-dbab-459e-8192-89da093a8b19)
_(The gif may render slower than the actual speed!)_


### Using our own Custome UI!
As a full-stack engineer, I couldn't help but include a basic UI built using [Flask](https://flask.palletsprojects.com/en/3.0.x/) for a richer experience. Follow these steps to explore:
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
![f846c788-a640-4a6e-af17-3cedeebe5d07](https://github.com/ThusharaN/SciBot/assets/85170859/90ba0725-9320-46bb-aef4-494a816872d1)
_(The gif may render slower than the actual speed!)_


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


## <u>Limitations</u>
