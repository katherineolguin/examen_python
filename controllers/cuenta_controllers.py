from flask import render_template, redirect, request, session, flash
from flask_app import app


from flask_app.models.cuenta import Cuenta



@app.route('/')
def index():


    return render_template('index.html' )


@app.route('/dashboard')
def dashboard():

    if 'cliente_id' not in session:
        return redirect('/')

    #Yo sé que en sesión tengo el id de mi usuario (session['cliente_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['cliente_id']}

    cliente = Cuenta.get_by_id(formulario)


    return render_template('dashboard.html', cliente=cliente )
    # return render_template('dashboard.html')



@app.route('/log', methods=['POST'] )
def log():

    cliente = Cuenta.get_by_nombre(request.form)

    if not cliente: #Si user = False / sino se cumple con esta funcion sigue con a sigiente y la siguiente y así
        flash('nombre no encontrado', 'log')
        return redirect('/')


    session['cliente_id'] = cliente.id

    return redirect('/dashboard')
