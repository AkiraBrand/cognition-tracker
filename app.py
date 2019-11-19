from flask import Flask
app = Flask(__name__)
import schema


@app.route('/')

def welcome():
    return "Welcome to Cognition Tracker!"

@app.route('/new')

def new():
    return "This is a new page!"

@app.route('/overview')

def overview():
    return "Here is your overview"

if __name__ == "__main__":
    app.run(debug=True)
