from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'moussaillon'}
    lists = [
        {
            'author': {'username': 'Garag'},
            'name': 'La bande à Dudule',
            'faction': 'Sundars',
            'format': '1000 PO'
        },
        {
            'author': {'username': 'Manu'},
            'name': 'Le Cartel de Nachos de la Riviera',
            'faction': 'Quintors',
            'format': '400 PO'
        }
    ]
    return render_template('index.html', title='Briskars', user=user, lists=lists)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)