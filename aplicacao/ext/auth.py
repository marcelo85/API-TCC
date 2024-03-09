from flask_simplelogin import SimpleLogin, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from aplicacao.ext.database import db
from aplicacao.models import User


def verifica_login(user):
    """Valida o usuário e senha para efetuar o login"""
    usuario = user.get("usuario")
    senha = user.get("senha")

    if not usuario or not senha:
        return False
    usuario_existe = User.query.filter_by(username=usuario).first()
    if not usuario_existe:
        return False
    if check_password_hash(usuario_existe.password, senha):
        return True
    return False


def cria_usuario(username, password):
    """Cria um usuário"""
    if User.query.filter_by(username=username).first():
        raise RuntimeError(f'{username} já está cadastrado')
    user = User(username=username, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return user


def init_app(app):
    SimpleLogin(app, login_checker=verifica_login)
