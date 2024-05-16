# render temlate for final document
from email import message
from flask import Flask, jsonify, render_template, request

from chat import get_response


app=Flask(__name__)

@app.get("/")
def index_get():
    return render_template("index.html")


    

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response=get_response(text)
    message={"answer":response}
    return jsonify(message)

@app.route('/help_yourself')
def help_yourself():
    return render_template('help-yourself.html')

@app.route('/educate_yourself')
def educate_yourself():
    return render_template('educate-yourself.html')

@app.route('/help_others')
def help_others():
    return render_template('help-others.html')


@app.route('/spread_the_word')
def spread_the_word():
    return render_template('spread-the-word.html')


@app.route('/sign_up')
def sign_up():
    return render_template('sign-up.html')


@app.route('/sign_in')
def sign_in():
    return render_template('sign-in.html')










if __name__ == "__main__":
    app.run(debug=True)
