from flask import render_template, flash, redirect, url_for
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)