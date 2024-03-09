from flask import Flask, render_template

app = Flask(__name__)

app.config['TITLE'] = 'Meu site'


@app.route('/')
def index():
    animais = ['Coiote', 'Lince Pardo', 'Veado da Virgínia']
    return render_template('index.html', animais=animais)
