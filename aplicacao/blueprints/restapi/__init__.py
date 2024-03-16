from flask import Blueprint
from flask_restful import Api

from aplicacao.blueprints.restapi.resources import AnimaisResource, AnimaisItemResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)
api.add_resource(AnimaisResource, "/animais/")
api.add_resource(AnimaisItemResource, "/animais/<int:animal_id>")


def init_app(app):
    app.register_blueprint(bp)
