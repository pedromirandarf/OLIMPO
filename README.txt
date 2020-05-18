ARQUVIVO PARA UTILIZAÇÃO DA APLICAÇÃO 


AUTOR: PEDRO CELSO MIRANDA ROCHA FILHO 


COMO INSTALAR O PIP3

$ sudo apt-get install pip3

COMO INSTALAR O VENV

$ pip3 install virtualenv

CRIAR UM NOVO AMBIENTE --> CRIAR UMA PASTA PRIMEIRO

$ virtualenv -p python3 projeto

ENTRAR NO AMBIENTE VIRTUAL 

$ . ihc/bin/activate

INSTALAR O FLASK

$ ihc/bin/pip3 install Flask 

COMANDO FREEZE

$ ihc/bin/pip3 freeze > requirements.txt


INSTALAR O SQLALchemy NA APLICAÇÃO 

$ ihc/bin/pip3 install flask-sqlalchemy

INSTALAR O FLASK MIGRATE 

$ ihc/bin/pip3 install flask-migrate

INSTALAR O FLASK-SCRIPT

$ ihc/bin/pip3 install flask-script

INSTALAR O WTS FORMS 

$ ihc/bin/pip3 install Flask-WTF

INTALAR O LOGIN DO FLASK

$ ihc/bin/pip3 install flask-login


#########################################################

COMANDOS IMPORTANTES

INICIAR A APLICAÇÃO 

python3 run.py runserver

ALTERAR O BANCO DE DADOS 

python3 run.py  db init 

python3 run.py  db migrate

python3 run.py  db upgrade






