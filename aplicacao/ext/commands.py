import click

from aplicacao import app
from aplicacao.ext.database import db
from aplicacao.ext.auth import cria_usuario
from aplicacao.models import Animais


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Animais(
            id=1, nome_cientifico="Canis latrans", nome_popular="Coiote", descricao="Coiote do deserto americano"
        ),
        Animais(id=2, nome_cientifico="Canis latrans", nome_popular="Coiote", descricao="Coiote da neve"),
        Animais(id=3, nome_cientifico="Canis latrans", nome_popular="Coiote", descricao="Coiote do pantano"),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Animais.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(usuario, senha):
        """Adds a new user to the database"""
        return cria_usuario(usuario, senha)