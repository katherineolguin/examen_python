

from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash




class Cuenta:
    

    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.numero_cuenta = data['numero_cuenta']
        self.saldo = data['saldo']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        


    @staticmethod
    def valido_nombre(formulario):

        es_valido =True


        if len(formulario['nombre'])<2:
            flash('El nombre debe contener mas caracteres', 'log')
            es_valido = False

        query = "SELECT * FORM clientes WHERE nombre = %(nombre)s"
        resultado = connectToMySQL('examen_python').query_db(query, formulario)

        if len(resultado) <1:
            flash('El nomrbe no se encuentra registrado', 'log')
            es_valido = False

        return es_valido

    



    @classmethod 
    def save(cls, formulario):
# deveriams hacer otra consulta my sql con usuario y cuenta aparte y colocar aqui los depositos returos y compras 
        query="INSERT INTO clientes (nombre, numero_cuenta, saldo, cliente_id) VALUES (%(nombre)s, %(numero_cuenta)s, %(saldo)s, %(cliente_id)s) "

        resultado= connectToMySQL('examen_python').query_db(query,formulario)
        return resultado


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM clientes"
        resultado = connectToMySQL('examen_python').query_db(query)

        cleintes=[]

        for cliente in resultado: 
            clientes.append(cls(cliente))


        return clientes


    @classmethod
    def get_by_id(cls, formulario):

        query= "SELECT * FROM clientes WHERE id = %(id)s"

        resultado = connectToMySQL('examen_python').query_db(query, formulario)

        cliente = cls(resultado[0])


        return cliente


# ESTE CODIGO SI SIRVIO 
    # @classmethod
    # def save_retiro(cls,formulario,cliente, saldo_retiro):

    #     cliente.cliente_retiro = 0


    #     cliente_r = cliente.cliente_retiro + saldo_retiro 
    #     # cliente_r += saldo_retiro
    #     # cliente_r.append(cliente.cliente_retiro)

    #     print(f'saldo retirado {cliente.cliente_retiro}')


    #     return cliente_r



# Esté codigo lo pasé por el class methods retiro

    # @classmethod
    # def save_retiro(cls, formulario, saldo_retiro):

    #         query_retiro = "SELECT retiro FROM examen_python.clientes  WHERE id = %(id)s"
    #         saldo_retiro_actual = connectToMySQL('examen_python').query_db(query_retiro, formulario)[0]['retiro'] 
    #         # 1° hago mi query, luego mando la consulta y hago la conexion con mi base de datos
    #         # Con esto => formulario)[0]['saldo'] --> Me devuelve los valores de el ID del cliente y accedo a este con [0] y espesificamente al saldo ['saldo']

    #         new_saldo_retiro = int(saldo_retiro_actual) + (saldo_retiro)
                

    #         query = "UPDATE examen_python.clientes SET retiro =  %(new_saldo_retiro)s  WHERE id = %(id)s"
    #         data = {'new_saldo_retiro':new_saldo_retiro, 'id': formulario['id']}
    #         # Aquí establecemos los valores de las Keys 'new_saldo' y 'id', los que serian el valor total eñ nuevo saldo y el ID del cliente que accdedimos a travez del formulario.
    #         cliente_retiro = connectToMySQL('examen_python').query_db(query,data)
            
    #         if new_saldo_retiro + 1:
    #             print(f"Tienes un giro de ${saldo_retiro} ")
    #         else:
    #             print("Error al actualizar el recarga en la base de datos")
            
    #         return cliente_retiro

        

        # cliente.cliente_retiro += saldo_retiro  # Actualizar el valor de cliente_retiro en la instancia de cliente

        # return cliente.cliente_retiro




    @classmethod
    def get_by_nombre(cls, formulario):

        query="SELECT * FROM clientes WHERE nombre = %(nombre)s"

        resultado= connectToMySQL('examen_python').query_db(query, formulario)
        
        if len(resultado) < 1:

            return False
        
        else:

            cliente = cls(resultado[0])

            return cliente




    @classmethod
    def deposito_update(cls,saldo_recarga,formulario):

            query_saldo = "SELECT saldo FROM examen_python.clientes  WHERE id = %(id)s"
            saldo_actual = connectToMySQL('examen_python').query_db(query_saldo, formulario)[0]['saldo'] 
            # 1° hago mi query, luego mando la consulta y hago la conexion con mi base de datos
            # Con esto => formulario)[0]['saldo'] --> Me devuelve los valores de el ID del cliente y accedo a este con [0] y espesificamente al saldo ['saldo']

            new_saldo = int(saldo_actual) + (saldo_recarga)
                

            query = "UPDATE examen_python.clientes SET saldo =  %(new_saldo)s  WHERE id = %(id)s"
            data = {'new_saldo': new_saldo, 'id': formulario['id']}
            # Aquí establecemos los valores de las Keys 'new_saldo' y 'id', los que serian el valor total eñ nuevo saldo y el ID del cliente que accdedimos a travez del formulario.

            resultado = connectToMySQL('examen_python').query_db(query,data)
            
            if new_saldo + 1:
                print(f"Tienes un deposito de ${saldo_recarga} ")
            else:
                print("Error al actualizar el recarga en la base de datos")
            
            return resultado



# -------------------------------------------------
# descontamos el retiro al saldo actual y lo actualizamos con el nuevo saldo

    @classmethod
    def retiro_update(cls,saldo_retiro,formulario):

            query_saldo = "SELECT saldo FROM examen_python.clientes  WHERE id = %(id)s"
            saldo_actual = connectToMySQL('examen_python').query_db(query_saldo, formulario)[0]['saldo'] 
            # 1° hago mi query, luego mando la consulta y hago la conexion con mi base de datos
            # Con esto => formulario)[0]['saldo'] --> Me devuelve los valores de el ID del cliente y accedo a este con [0] y espesificamente al saldo ['saldo']

            new_saldo = int(saldo_actual) - (saldo_retiro)
                

            query = "UPDATE examen_python.clientes SET saldo =  %(new_saldo)s  WHERE id = %(id)s"
            data = {'new_saldo': new_saldo, 'id': formulario['id']}
            # Aquí establecemos los valores de las Keys 'new_saldo' y 'id', los que serian el valor total eñ nuevo saldo y el ID del cliente que accdedimos a travez del formulario.

            resultado = connectToMySQL('examen_python').query_db(query,data)
            
            if new_saldo + 1:
                print(f"Tienes un giro de ${saldo_retiro} ")
            else:
                print("Error al actualizar el recarga en la base de datos")
            
            return resultado

# ----------------------------------------------------
# descuento la compra al saldo del cliente y actualizo su saldo 
    @classmethod
    def compra_update(cls,saldo_compra,formulario):

            query_saldo = "SELECT saldo FROM examen_python.clientes  WHERE id = %(id)s"
            saldo_actual = connectToMySQL('examen_python').query_db(query_saldo, formulario)[0]['saldo'] 
            # 1° hago mi query, luego mando la consulta y hago la conexion con mi base de datos
            # Con esto => formulario)[0]['saldo'] --> Me devuelve los valores de el ID del cliente y accedo a este con [0] y espesificamente al saldo ['saldo']

            new_saldo = int(saldo_actual) - (saldo_compra)
                

            query = "UPDATE examen_python.clientes SET saldo =  %(new_saldo)s  WHERE id = %(id)s"
            data = {'new_saldo': new_saldo, 'id': formulario['id']}
            # Aquí establecemos los valores de las Keys 'new_saldo' y 'id', los que serian el valor total eñ nuevo saldo y el ID del cliente que accdedimos a travez del formulario.

            resultado = connectToMySQL('examen_python').query_db(query,data)
            
            if new_saldo + 1:
                print(f"Tienes un giro de ${saldo_compra} ")
            else:
                print("Error al actualizar el recarga en la base de datos")
            
            return resultado