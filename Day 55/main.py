from flask import Flask
import random as rd


def style_h1(function):
    colors = ["red", "green", "blue", "orange", "yellow", "black", "pink",
              "purple", "brown", "grey"]

    def style(**kwargs):
        return f"<style> h1 {{color: {colors[kwargs['number']]}}}</style> {function(kwargs['number'])} "

    return style


app = Flask(__name__)


@app.route('/<int:number>')
@style_h1
def guess_the_number(number):
    if number == random_number:
        return "<h1>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

    if number < random_number:
        return "<h1>Is to low!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"

    else:
        return "<h1>Is too high!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


random_number = rd.randint(0, 9)
