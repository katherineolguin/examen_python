from flask import render_template, redirect, request, session, flash
from flask_app import app

from datetime import datetime  #Manipular fechas

from flask_app.models.cuenta import Cuenta
from flask_app.models.retiro import Retiro



@app.route('/retiro', methods=['POST'])
def retiro():

    if 'cliente_id' not in session:
        return redirect('/')


    formulario = {"id": session['cliente_id']}




    # ------------------------------
    saldo_retiro = int(request.form['retiro'])  

    
    #------------------------
# Actualiza el saldo de la cuenta  
    resultado= Cuenta.retiro_update(saldo_retiro, formulario)
# -----------------------------------------
    # Suma y actualiza el total del retiro
    cliente_retiro = Retiro.save_retiro(formulario,saldo_retiro)

# -----------------------------------
    # Me agrega un nuevo retiro a la base de datos de Retiros, creando un nueo diccionario en el cual integro " 'retiro': int(request.form['retiro']) "del formulario, yaque, no puedo integrarlo por separado como  "salo_retiro" ya que no queda en claro que este es igual a la key retiro de mi SQL

    formulario_retiro = {
        'retiro': int(request.form['retiro']),
        # 'detalle': request.form['detalle'],
        'created_at': datetime.now(),
        'updated_at': datetime.now(),
        'cliente_id': session['cliente_id']
    }




    Retiro.new_retiro(formulario_retiro)



    # ---------------------------
    return redirect('/dashboard')






@app.route('/comprar', methods=['POST'])
def comprar():
    if 'cliente_id' not in session:
        return redirect('/')


    formulario = {"id": session['cliente_id']}

    saldo_compra = int(request.form['retiro'])  

    formulario_compra = {
        'retiro': int(request.form['retiro']),
        'detalle': request.form['detalle'],
        'created_at': datetime.now(),
        'updated_at': datetime.now(),
        'cliente_id': session['cliente_id']
    }

    resultado = Cuenta.compra_update(saldo_compra,formulario)

    cliente_compra = Retiro.save_compra(formulario, saldo_compra)

    Retiro.new_compra(formulario_compra)



    # ---------------------------
    return redirect('/dashboard')





















#   ESTO SIRVIO 
#  @classmethod
#     def get_fechas(cls):
#         query = "SELECT id, created_at, updated_at, cliente_id FROM retiros WHERE id <> 1 "

#         resultado = connectToMySQL('examen_python').query_db(query)

#         fecha_retiro=[]

#         for fecha in resultado:

#             # (Esto y especificamente poner "retiro" en nuestro diccionario, es lo mismo que poner el "cls" (datos_retiro.append(cls(retiro)) cuando hagamos nuestro append)

#             id         = fecha ['id']
#             created_at = fecha['created_at']
#             updated_at = fecha['updated_at']
#             cliente_id = fecha ['cliente_id']

#             # Estos datos lo pasamos como diccionario, en cada iteración con las claves correspondientes y los valores asociados. Esto permite agregar cada diccionario a la lista datos_retiro como un elemento independiente

#             fecha_retiro.append({

#                 'id'          : id,
#                 'created_at'  : created_at.strftime("%d-%m-%Y %H:%M:%S"), 
#                 'updated_at'  : updated_at.strftime("%d-%m-%Y %H:%M:%S"), 
#                 'cliente_id'  : cliente_id
#                 })

            

            
#             # datos_retiro.append(cls(retiro))


#         return fecha_retiro


