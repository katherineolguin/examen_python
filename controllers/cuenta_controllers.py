from flask import render_template, redirect, request, session, flash
from flask_app import app


from flask_app.models.cuenta import Cuenta



@app.route('/')
def index():

    cliente = Cuenta.get_by_id(cls)




    return render_template('index.html' , cliente=cliente)


@app.route('/log', methods=['POST'] )
def log():

    cliente = Cuenta.get_by_id(formulario)

    return render_template('log.html', cliente=cliente)
