from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    animais = ['Coiote', 'Lince Pardo', 'Veado da Virgínia']
    return animais[0]