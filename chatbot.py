from flask import Flask, render_template, request, jsonify
from qamodel import ScienceChatBot

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    SEPERATOR = '\n'
    if request.method == 'POST':
        # Converting the string input into a list of strings (questions)
        user_message = str(request.json['user_message'])
        user_message = user_message.split(SEPERATOR)

        # Instantiating the ScienceChatBot class to predict the answers
        chatbot = ScienceChatBot()
        answers = chatbot.predict_answer(user_message)

        # Returning json response to be rendered in the chatbot
        chatbot_response = SEPERATOR.join(answers)
        return jsonify({'message': chatbot_response})

    return render_template('index.html')
