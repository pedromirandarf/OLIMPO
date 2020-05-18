from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=True) 
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    cpf = db.Column(db.String)
    diretoria=db.Column(db.String)
    email_p = db.Column(db.String)
    cidade = db.Column(db.String)
    pais = db.Column(db.String)
    endereco = db.Column(db.String)
    sobrenome = db.Column(db.String)
    sobre_mim = db.Column(db.Text)
    data_aniver = db.Column(db.String)
    image = db.Column(db.String)
    cep = db.Column(db.String)
    cargo = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
    
    

    def __init__(self, username, password, name,email,cpf,diretoria,email_p,cidade,pais,cep,endereco,sobrenome,sobre_mim, data_aniver,image, cargo):
        self.username = username
        self.password = password
        self.name =  name
        self.email = email
        self.cpf = cpf
        self.diretoria = diretoria
        self.email_p = email_p
        self.cidade = cidade
        self.pais = pais
        self.cep = cep
        self.endereco = endereco
        self.sobrenome = sobrenome
        self.sobre_mim = sobre_mim
        self.data_aniver = data_aniver
        self.image = image
        self.cargo = cargo

    def __repr__(self):
        return "<User %r>" % self.username

class Projetos(db.Model):
    __tablename__ = "projetos"
    id = db.Column(db.Integer, primary_key=True)
    diretoria = db.Column(db.String)
    content = db.Column(db.Text)
    empresa = db.Column(db.String)
    valor = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', foreign_keys=user_id)
    duracao = db.Column(db.String)
    
    def __init__(self, diretoria,content,empresa,valor,duracao,user_id ):
        self.content = content
        self.user_id = user_id
        self.diretoria = diretoria
        self.empresa = empresa
        self.valor = valor
        self.duracao = duracao
        



def __repr__(self):
    return "<Post %r>" % self.id

class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    uer = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)


    