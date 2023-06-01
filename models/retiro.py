
from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
from datetime import datetime  #Manipular fechas

from flask_app.models.cuenta import Cuenta



class Retiro:

    def __init__(self,data):
        
        self.id = data['id']
        self.retiro =data['retiro']
        self.detalle = data['detalle']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.cliente_id = data['cliente_id']


    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM retiros WHERE id <> 1 "

    #     resultado = connectToMySQL('examen_python').query_db(query)

    #     datos_retiro=[]

    #     for retiro in resultado: 

    #         datos_retiro.append(cls(retiro))


    #     return datos_retiro

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM retiros WHERE id <> 1  ORDER BY id DESC"

        resultado = connectToMySQL('examen_python').query_db(query)

        datos_retiro=[]

        for iteracion_retiro in resultado:

            # (Esto y especificamente poner "retiro" en nuestro diccionario, es lo mismo que poner el "cls" (datos_retiro.append(cls(retiro)) cuando hagamos nuestro append)

        
            id         = iteracion_retiro ['id']
            retiro     = iteracion_retiro['retiro']
            # detalle    = retiro['detalle']
            created_at = iteracion_retiro['created_at']
            updated_at = iteracion_retiro['updated_at']
            cliente_id = iteracion_retiro ['cliente_id']

            # Estos datos lo pasamos como diccionario, en cada iteración con las claves correspondientes y los valores asociados. Esto permite agregar cada diccionario a la lista datos_retiro como un elemento independiente

            datos_retiro.append({

                'id'          : id,
                'retiro'      : retiro,
                # 'detalle'     :detalle,
                'created_at'  : created_at.strftime("%d de %b %Y  %H:%M hr"), 
                'updated_at'  : updated_at.strftime("%d-%m-%Y %H:%M:%S"), 
                'cliente_id'  : cliente_id
                })

            # datos_retiro.append(cls(retiro))

        return datos_retiro





    @classmethod
    def new_retiro(cls, formulario_retiro):

        query = "INSERT INTO retiros (retiro,created_at, updated_at,  cliente_id) VALUES (%(retiro)s,%(created_at)s,%(updated_at)s,  %(cliente_id)s )"

        


        result = connectToMySQL('examen_python').query_db(query, formulario_retiro)
        return result



    @classmethod
    def get_by_id(cls, formulario):

        query= "SELECT * FROM retiros WHERE id = %(id)s"

        resultado = connectToMySQL('examen_python').query_db(query, formulario)

        retiro_cliente = cls(resultado[0])


        return retiro_cliente

    @classmethod
    def save_retiro(cls, formulario, saldo_retiro):

            query_retiro = "SELECT retiro FROM examen_python.retiros  WHERE id = %(id)s"
            saldo_retiro_actual = connectToMySQL('examen_python').query_db(query_retiro, formulario)[0]['retiro'] 
            # 1° hago mi query, luego mando la consulta y hago la conexion con mi base de datos
            # Con esto => formulario)[0]['saldo'] --> Me devuelve los valores de el ID del cliente y accedo a este con [0] y espesificamente al saldo ['saldo']

            new_saldo_retiro = int(saldo_retiro_actual) + (saldo_retiro)
                

            query = "UPDATE examen_python.retiros SET retiro =  %(new_saldo_retiro)s  WHERE id = %(id)s"
            data = {'new_saldo_retiro':new_saldo_retiro, 'id': formulario['id']}
            # Aquí establecemos los valores de las Keys 'new_saldo' y 'id', los que serian el valor total eñ nuevo saldo y el ID del cliente que accdedimos a travez del formulario.
            cliente_retiro = connectToMySQL('examen_python').query_db(query,data)
            
            if new_saldo_retiro + 1:
                print(f"Tienes un giro de ${saldo_retiro} ")
            else:
                print("Error al actualizar el recarga en la base de datos")
            
            return cliente_retiro




#----------------- ----------------------------------
# agregar nuevo retiro a mi base de datos "retiros"
    @classmethod
    def new_compra(cls, formulario_compra):

        query = "INSERT INTO retiros (retiro,detalle,created_at, updated_at,  cliente_id) VALUES (%(retiro)s,%(detalle)s,%(created_at)s,%(updated_at)s,  %(cliente_id)s )"

        


        result = connectToMySQL('examen_python').query_db(query, formulario_compra)

        return result


# --------------------------------------
# Agrego el nuevo retiro y lo sumo con los demas retiros de mi base de datos, luego actualizo los datos
    @classmethod
    def save_compra(cls, formulario, saldo_compra):

            query_retiro = "SELECT retiro FROM examen_python.retiros  WHERE id = %(id)s"

            saldo_retiro_actual = connectToMySQL('examen_python').query_db(query_retiro, formulario)[0]['retiro'] 
            # 1° hago mi query, luego mando la consulta y hago la conexion con mi base de datos
            # Con esto => formulario)[0]['saldo'] --> Me devuelve los valores de el ID del cliente y accedo a este con [0] y espesificamente al saldo ['saldo']

            new_saldo_compra_mas_retiro = int(saldo_retiro_actual) + (saldo_compra)
                

            query = "UPDATE examen_python.retiros SET retiro =  %(new_saldo_compra_mas_retiro)s  WHERE id = %(id)s"

            data = {'new_saldo_compra_mas_retiro':new_saldo_compra_mas_retiro, 'id': formulario['id']}
            # Aquí establecemos los valores de las Keys 'new_saldo' y 'id', los que serian el valor total eñ nuevo saldo y el ID del cliente que accdedimos a travez del formulario.
            cliente_compra = connectToMySQL('examen_python').query_db(query,data)
            
            if new_saldo_compra_mas_retiro + 1:
                print(f"Tienes un giro de ${saldo_compra} ")
            else:
                print("Error al actualizar el recarga en la base de datos")
            
            return cliente_compra

    @classmethod
    def get_all_compras(cls):
        query = "SELECT id, retiro, detalle, cliente_id, created_at, updated_at FROM retiros WHERE detalle IS NOT NULL ORDER BY id DESC"

        resultado = connectToMySQL('examen_python').query_db(query)

        datos_compra=[]

        for compra in resultado: 

        # (Esto y especificamente poner "retiro" en nuestro diccionario, es lo mismo que poner el "cls" (datos_retiro.append(cls(retiro)) cuando hagamos nuestro append)

    
            id         = compra ['id']
            retiro     = compra['retiro']
            detalle    = compra['detalle']
            created_at = compra['created_at']
            updated_at = compra['updated_at']
            cliente_id = compra ['cliente_id']

            # Estos datos lo pasamos como diccionario, en cada iteración con las claves correspondientes y los valores asociados. Esto permite agregar cada diccionario a la lista datos_retiro como un elemento independiente

            datos_compra.append({

                'id'          : id,
                'retiro'      : retiro,
                'detalle'     :detalle,
                'created_at'  : created_at.strftime("%d de %b %Y  %H:%M hr"), 
                'updated_at'  : updated_at.strftime("%d-%m-%Y %H:%M:%S"), 
                'cliente_id'  : cliente_id
                })



        # datos_compra.append(cls(compra))


        return datos_compra





