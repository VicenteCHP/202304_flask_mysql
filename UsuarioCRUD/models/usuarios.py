"""Usuarios models."""

# Utils
from utils.mysql_connection import connectToMySQL


class Usuario:

    def __init__(self, data):

        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.correo_electronico = data["correo_electronico"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):

        query = """SELECT * FROM usuarios;"""
        resultados = connectToMySQL("usuariosdb_schema").query_db(query)
        usuarios = []
        for resultado in resultados:
            usuarios.append(cls(resultado))
        return usuarios

    @classmethod
    def get_one(cls, data):

        query = """SELECT * FROM usuarios WHERE id = %(id)s;"""
        resultado = connectToMySQL("usuariosdb_schema").query_db(query, data)
        return cls(resultado[0])

    @classmethod
    def create(cls, data):

        query = """
        INSERT INTO usuarios (nombre, apellido, correo_electronico)
        VALUES (%(nombre)s, %(apellido)s, %(correo_electronico)s);
        """
        resultado = connectToMySQL("usuariosdb_schema").query_db(query, data)
        return resultado

    @classmethod
    def update(cls, data):

        query = """
        UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, correo_electronico = %(correo_electronico)s
        WHERE id = %(id)s;
        """
        return connectToMySQL("usuariosdb_schema").query_db(query, data)

    @classmethod
    def delete(cls, data):

        query = """
        DELETE FROM usuarios WHERE id = %(id)s;
        """
        return connectToMySQL("usuariosdb_schema").query_db(query, data)
