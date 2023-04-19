from flask_app.config.mysqlconnection import connectToMySQL



class Cuenta:



    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.numero_cuenta = data['numero_cuenta']
        self.saldo = data['saldo']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM clientes"
        resultado = connectToMySQL('examen_python').query_db(query)

        cleintes=[]

        for cliente in resultado: 
            clientes.append(cls(cliente))


        return clientes


    @classmethod
    def get_by_id(cls):

        query= "SELECT * FROM clientes WHERE id = %(id)s"

        result = connectToMySQL('examen_python').query_db(query, formulario)

        cliente = cls(result[0])

        return cliente



    @classmethod
    def deposito(cls, recarga):
        query = "SELECT saldo FROM clientes WHERE id = %(id)s;"
        resultado = connectToMySQL('examen_python').query_db(query)

        self.saldo += recarga

        if self.saldo + 1:
            print(f"Tienes un deposito de $+{recarga}")

            return self


        
    @classmethod
    def deposito(cls, compra):
        query = "SELECT saldo FROM clientes WHERE id = %(id)s;"
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









