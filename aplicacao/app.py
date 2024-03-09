from flask import Flask, abort, render_template
from aplicacao.ext import configuration
from aplicacao.ext import appearance
from aplicacao.ext import database
from aplicacao.ext import auth
from aplicacao.ext import admin
from aplicacao.ext import commands

app = Flask(__name__)

configuration.init_app(app)
appearance.init_app(app)
database.init_app(app)
auth.init_app(app)
admin.init_app(app)
commands.init_app(app)



admin.add_view(sqla.ModelView(Animal, db.session))


@app.cli.command()
def create_db():
    """Creates sqlite database"""
    db.create_all()


@app.route("/")
def index():
    animais = Animal.query.all()
    return render_template("index.html", animais=animais)


@app.route("/animal/<animal_id>")
def animal(animal_id):
    animais = Animal.query.filter_by(id=animal_id).first() or abort(
        404, "Animal não encontrado"
    )
    return render_template("animal.html", animal=animais)
