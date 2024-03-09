from aplicacao.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_cientifico = db.Column(db.String(20))
    nome_popular = db.Column(db.String(20))
    descricao = db.Column(db.Text())


class Usuario(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(140))
    senha = db.Column(db.String(512))