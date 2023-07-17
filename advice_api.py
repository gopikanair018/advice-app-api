from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
# This line creates an instance of the Flask class and assigns it to the variable app. The __name__ argument is a special Python variable that represents the name of the current module. 

CORS(app)
# This line initializes the Flask-CORS extension with the app instance
@app.route('/caption', methods=['GET'])
def get_advice():
    advices = [
        "Take time to know yourself",
        "A narrow focus brings big results",
        "Show up fully",
       "Be patient and persistent",
       "In order to get, you have to give",
       "Luck comes from hard work",
       "Be your best at all times",
       "Don't try to impress everyone",
       "Don't be afraid of being afraid",
       "Listen to learn",
       "Life's good, but it's not fair",
       "No task is beneath you",
       "You can't always get what you want",
       "Don't make decisions when you are angry or ecstatic",
       "Don't worry what other people think",
       "Use adversity as an opportunity",
       "Do what is right, not what is easy",
       "Dreams remain dreams until you take action",
       "Treat others the way you want to be treated",
       "When you quit, you fail"
    ]
    advice = random.choice(advices)
    return jsonify({'advice': advice})

if __name__ == '__main__':
    app.run()
