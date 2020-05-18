from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, FloatField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class USER_UPDATE(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    cpf = StringField("cpf", validators=[DataRequired()])
    diretoria = StringField("diretoria", validators=[DataRequired()])
    email_p = StringField("email_p", validators=[DataRequired()])
    cidade = StringField("cidade", validators=[DataRequired()])
    pais = StringField("pais", validators=[DataRequired()])
    endereco = StringField("endereco", validators=[DataRequired()])
    sobrenome = StringField("sobrenome", validators=[DataRequired()])
    sobre_mim = StringField("sobre_mim", validators=[DataRequired()])
    data_aniver = StringField("data_aniver", validators=[DataRequired()])
    cep = StringField("data_aniver", validators=[DataRequired()])
    cargo = StringField("data_aniver", validators=[DataRequired()])
    image = StringField("image")




class CadastroProj(FlaskForm):
    diretoria = StringField("diretoria", validators=[DataRequired()])
    content = StringField("content", validators=[DataRequired()])
    empresa = StringField("empresa", validators=[DataRequired()])
    valor = FloatField("valor", validators=[DataRequired()])
    duracao = StringField("duracao", validators=[DataRequired()])