import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join (basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'senha-bem-segura'

IMAGE_UPLOADS = "/home/pedro/Área de Trabalho/Matérias 2019.1/IHC/Projeto 2/app/static/uploads"
