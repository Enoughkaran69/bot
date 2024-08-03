from flask import Flask, jsonify
import random

app = Flask(__name__)

messages = [
    "Hello, world!",
    "How are you today?",
    "Keep going, you're doing great!",
    "Have a fantastic day!",
    "Believe in yourself!",
    "You're amazing!",
]

@app.route('/random_message', methods=['GET'])
def random_message():
    return jsonify({"message": random.choice(messages)})

if __name__ == '__main__':
    app.run()
