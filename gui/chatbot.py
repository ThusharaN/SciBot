from flask import Flask, render_template, request, jsonify
import asyncio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_message = str(request.json['user_message'])
        user_message = user_message.split("\n")
        # chatbot_response = your_chatbot_function(user_message)
        # return jsonify({'message': chatbot_response})

        # Define an asynchronous function to handle chatbot response
        async def get_chatbot_response():
            chatbot_response = await asyncio.to_thread(your_chatbot_function, user_message)
            return chatbot_response

        # Use asyncio.run to execute the asynchronous function
        chatbot_response = asyncio.run(get_chatbot_response())

        return jsonify({'message': chatbot_response})

    return render_template('index.html')

# Define your_chatbot_function based on your actual implementation
def your_chatbot_function(user_message):
    # Replace this with your chatbot logic
    return "Thank you for your question. I'll get back to you soon!"


# @app.route('/')
# def hello():
#     return 'Hello, World!'