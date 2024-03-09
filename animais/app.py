from dynaconf import FlaskDynaconf
from flask import Flask, abort, render_template
from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_bootstrap import Bootstrap
from flask_simplelogin import SimpleLogin, login_required
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
FlaskDynaconf(app)
Bootstrap(app)
db = SQLAlchemy(app)


def verifica_login(user):
    return user.get("usuario") == 'admin' and user.get("senha") == '123'


SimpleLogin(app, login_checker=verifica_login)

# Proteger o admin com login via Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)
admin = Admin(app, name=app.config.TITLE, template_mode="bootstrap3")


class Animais(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_cientifico = db.Column(db.String(20))
    nome_popular = db.Column(db.String(20))
    descricao = db.Column(db.Text())


admin.add_view(sqla.ModelView(Animais, db.session))


@app.cli.command()
def create_db():
    """Creates sqlite database"""
    db.create_all()


@app.route("/")
def index():
    animais = Animais.query.all()
    return render_template("index.html", animais=animais)


@app.route("/animal/<animal_id>")
def animal(animal_id):
    animal = Animais.query.filter_by(id=animal_id).first() or abort(
        404, "Animal não encontrado"
    )
    return render_template("animal.html", animal=animal)
