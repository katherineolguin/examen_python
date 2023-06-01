from flask import render_template, redirect, request, session, flash
from flask_app import app
from datetime import datetime  #Manipular fechas




from flask_app.models.cuenta import Cuenta
from flask_app.models.retiro import Retiro



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

    retiro_cliente = Retiro.get_by_id(formulario)

    datos_retiro = Retiro.get_all()

    datos_compra = Retiro.get_all_compras()


    # fecha_retiro = Retiro.get_fechas()






    return render_template('dashboard.html', cliente=cliente, retiro_cliente = retiro_cliente, datos_retiro = datos_retiro, datos_compra=datos_compra)
    # return render_template('dashboard.html')



@app.route('/log', methods=['POST'] )
def log():

    cliente = Cuenta.get_by_nombre(request.form)

    if not cliente: #Si user = False / sino se cumple con esta funcion sigue con a sigiente y la siguiente y así
        flash('nombre no encontrado', 'log')
        return redirect('/')


    session['cliente_id'] = cliente.id

    return redirect('/dashboard')





#            ESTE ES ACTUALIZA
@app.route('/deposito', methods=['POST'])
def deposito():
    if 'cliente_id' not in session:
        return redirect('/')

    print(request.form)

    formulario = {"id": session['cliente_id']}

    # Obtener la cuenta por el ID del cliente
    # cuenta = Cuenta.get_by_id(formulario['id'])
# ---------------------------------------------
    # Obtener la cantidad de dinero a depositar del formulario
    saldo_recarga = int(request.form['saldo'])

    # Actualizar el saldo en la cuenta
    resultado = Cuenta.deposito_update(saldo_recarga, formulario)
# -----------------------------------------------
    return redirect('/dashboard')



