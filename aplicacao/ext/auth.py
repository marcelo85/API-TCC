from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash
from aplicacao.ext.database import db
from aplicacao.models import Usuario


def verifica_login(user):
    """Valida o usuário e senha para efetuar o login"""
    usuario = user.get("usuario")
    senha = user.get("senha")

    if not usuario or not senha:
        return False
    usuario_existe = Usuario.query.filter_by(usuario=usuario).first()
    if not usuario_existe:
        return False
    if check_password_hash(usuario_existe.password, senha):
        return True
    return False


def cria_usuario(usuario, senha):
    """Registra um novo usuario caso nao esteja cadastrado"""
    if Usuario.query.filter_by(usuario=usuario).first():
        raise RuntimeError(f'{usuario} ja esta cadastrado')
    usuario = Usuario(usuario=usuario, senha=generate_password_hash(senha))
    db.session.add(usuario)
    db.session.commit()
    return usuario


def init_app(app):
    SimpleLogin(app, login_checker=verifica_login)
