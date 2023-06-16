from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html.jinja')

@app.route('/ekstraktor')
def ekstraktor():
    return render_template('ekstraktor.html.jinja')

@app.route('/lista_produktow')
def lista_produktow():
    return render_template('lista_produktow.html.jinja')

@app.route('/produkt')
def produkt():
    return render_template('produkt.html.jinja')

@app.route('/charts')
def charts():
    return render_template('charts.html.jinja')

@app.route('/author')
def author():
    return render_template('author.html.jinja')