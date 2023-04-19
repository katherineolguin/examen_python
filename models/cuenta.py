from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash


class Cuenta:



    def __init__(self, data):
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

        query = "SELECT * FORM clientes WHERE nombre = %(nombre)s"
        resultado = connectToMySQL('examen_python').query_db(query, formulario)

        if len(resultado) <1:
            flash('El nomrbe no se encuentra registrado', 'log')

        return es_valido

        


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
    def deposito_update(cls, recarga):
        query = "UPDATE clientes SET saldo=%(saldo)s WHERE id = %(id)s;"
        resultado = connectToMySQL('examen_python').query_db(query)

        self.saldo += recarga

        if self.saldo + 1:
            print(f"Tienes un deposito de $+{recarga}")

            return self


        
    @classmethod
    def compra_update(cls, compra):
        query = "UPDATE clientes SET saldo=%(saldo)s WHERE id = %(id)s;"
        resultado = connectToMySQL('examen_python').query_db(query)

        self.saldo -= compra

        if self.saldo < compra:
            self.saldo = saldo_cliente
            print(f"Saldo insuficiente para generar la compra")
            return self

        else:

            print(f" Realizaste una compra de  $+{compra}")

            return self

    # def mostrar_detalles cuenta









