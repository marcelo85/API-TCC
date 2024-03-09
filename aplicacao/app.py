from flask import Flask
from aplicacao.ext import configuration
from aplicacao.ext import appearance
from aplicacao.ext import database
from aplicacao.ext import auth
from aplicacao.ext import admin
from aplicacao.ext import commands

from aplicacao.blueprints import views
from aplicacao.blueprints import restapi

app = Flask(__name__)

configuration.init_app(app)
appearance.init_app(app)
database.init_app(app)
auth.init_app(app)
admin.init_app(app)
commands.init_app(app)
views.init_app(app)
restapi.init_app(app)
