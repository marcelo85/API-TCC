from flask import render_template, abort

from aplicacao.models import Animais


def init_app(app):
    @app.route("/")
    def index():
        animais = Animais.query.all()
        return render_template("index.html", animais=animais)

    @app.route("/animal/<animal_id>")
    def animal(animal_id):
        animais = Animais.query.filter_by(id=animal_id).first() or abort(
            404, "Animal não encontrado"
        )
        return render_template("animal.html", animal=animais)
