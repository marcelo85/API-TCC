from flask import abort, jsonify
from flask_restful import Resource
from aplicacao.models import Animais


class ProductResource(Resource):
    def get(self):
        animais = Animais.query.all() or abort(204)
        return jsonify(
            {"products": [
                animal.to_dict()
                for animal in animais
            ]}
        )


class ProductItemResource(Resource):
    def get(self, animal_id):
        animal = Animais.query.filter_by(id=animal_id).first() or abort(
            404
        )
        return jsonify(animal.to_dict())
