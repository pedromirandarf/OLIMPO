from app import app
from flask import render_template, flash, url_for, redirect, request, session
from app.models.form import LoginForm, USER_UPDATE, CadastroProj
from app.models.tables import User, Projetos
from app import db,lm
from flask_login import login_user, logout_user, login_required
import os

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()



@app.route("/home/<info>")
@app.route("/home", defaults={"info":None})
@login_required
def home(info):
    #i = User("flavio@","12345", "pedro", "flavin@gmail.com")
    #db.session.add(i)
    #db.session.commit()
    projt = Projetos.query.filter_by().all()
    soma =0
    cont1 =0
    for projt1 in projt:
        soma = projt1.valor + soma
        cont1 = cont1 +1
    membros = User.query.filter_by().all()
    cont = 0
    for x in membros:
        cont = cont +1
    

    return render_template("dashboard.html", projt=projt, soma = soma,cont=cont,cont1=cont1, nome = session["kkk"])
    


@app.route("/login", methods=["GET","POST"])
@app.route("/", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            session["meuuser"] = user.id 
            session["kkk"] = user.name
            return redirect(url_for("home"))
            flash("VOCÊ ESTÁ LOGADO!")
        else:
            flash("LOGIN INVÁLIDO")
    else:
        print(form.errors)
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("Você foi deslogado")
    return redirect(url_for("login"))

@app.route("/new_account", methods=["GET","POST"])
def new_account():
    novo = USER_UPDATE()
    if novo.validate_on_submit():
        r = User(novo.username.data,novo.password.data, novo.name.data, novo.email.data, novo.cpf.data,novo.diretoria.data, novo.email_p.data, novo.cidade.data,
        novo.pais.data, novo.cep.data, novo.endereco.data, novo.sobrenome.data, novo.sobre_mim.data, novo.data_aniver.data, "NAO FUNCIONA",novo.cargo.data)
        db.session.add(r)
        db.session.commit()
        flash("Você foi cadastrado!")
        return redirect(url_for('new_account'))

    return render_template('new_account.html', novo=novo,nome = session["kkk"])


@app.route("/update", methods=["GET", "POST"])
@login_required
def update_profile():
    novo = USER_UPDATE()
    if request.method == "POST":

        if request.files:

            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
                
            
            r = User.query.filter_by(id=session.get("meuuser",None)).first()
            r.image= 'uploads/'+ image.filename
            print(r.image)
            db.session.add(r)
            db.session.commit()
            return redirect(url_for('update_profile'))

    if novo.validate_on_submit():
        r = User.query.filter_by(id=session.get("meuuser",None)).first()
        r.username = novo.username.data
        r.password = novo.password.data
        r.name = novo.name.data
        r.email = novo.email.data
        r.cpf = novo.cpf.data
        r.diretoria = novo.diretoria.data
        r.email_p = novo.email_p.data
        r.cidade = novo.cidade.data
        r.pais = novo.pais.data
        r.cep = novo.cep.data
        r.endereco = novo.endereco.data
        r.sobrenome = novo.sobrenome.data
        r.sobre_mim = novo.sobre_mim.data
        r.data_aniver = novo.data_aniver.data
        r.cargo = novo.cargo.data
        db.session.add(r)
        db.session.commit()
    else:
        print("vai tomar no cu")
    u = User.query.filter_by(id=session.get("meuuser",None)).first()
    sobrenome = u.sobrenome
    cargo = u.cargo
    print(u.image)
    perfil = u.image
    return render_template('update_profile.html',novo=novo,perfil=perfil,nome = session["kkk"], cargo = cargo,sobrenome=sobrenome)

@app.route("/membros")
@login_required
def membros():
    todos =  User.query.filter_by().all()
    presi = User.query.filter_by(diretoria='Presidência ' ).all() + User.query.filter_by(diretoria='Presidência' ).all() + User.query.filter_by(diretoria='presidencia' ).all() + User.query.filter_by(diretoria='presidência' ).all() 
    vp = User.query.filter_by(diretoria="Vice-Presidência").all() + User.query.filter_by(diretoria="vice-presidência").all() + User.query.filter_by(diretoria="vice-presidencia").all() + User.query.filter_by(diretoria="vice presidencia").all() +User.query.filter_by(diretoria="Vice Presidência").all()
    daf = User.query.filter_by(diretoria="Adm-Fin").all() + User.query.filter_by(diretoria="Administrativo Finaceiro").all()
    eel = User.query.filter_by(diretoria="eletrica").all() + User.query.filter_by(diretoria="Elétrica").all()
    eca = User.query.filter_by(diretoria="Eletrônica").all() + User.query.filter_by(diretoria="Eletronica").all() + User.query.filter_by(diretoria="eletrônica").all() + User.query.filter_by(diretoria="eletronica").all()
    eco = User.query.filter_by(diretoria="TI").all()
    return render_template('membros.html', todos=todos, presi=presi, vp=vp, daf=daf, eel=eel, eca=eca, eco=eco,nome = session["kkk"])


@app.route("/cadastro_projetos", methods=["GET","POST"])
@login_required
def cadastro_projetos():
    novo = CadastroProj()
    if novo.validate_on_submit():
        r = Projetos(novo.diretoria.data,novo.content.data, novo.empresa.data, novo.valor.data, novo.duracao.data,"1")
        db.session.add(r)
        db.session.commit()
        flash("Projeto cadastrado!")
        return redirect(url_for('cadastro_projetos'))

    return render_template('cadastro_projeto.html', novo=novo,nome = session["kkk"])

@app.route("/tutorial")
@login_required
def tutorial():
    return render_template('tutorial.html',nome = session["kkk"])

