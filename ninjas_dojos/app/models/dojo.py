from app.config.mysql_connection import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_ninjas').query_db(query)
        dojos = []
        for d in results:
            dojos.append(cls(d))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojo_ninjas').query_db(query, data)
        return result

    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojo_ninjas').query_db(query, data)
        print(results)
        if results:
            dojo = cls(results[0])
            for row in results:
                n = {
                    'id': row['id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'created_at': row['created_at'],
                    'updated_at': row['updated_at']
                }
                dojo.ninjas.append(Ninja(n))
            return dojo
        else:
            return None
