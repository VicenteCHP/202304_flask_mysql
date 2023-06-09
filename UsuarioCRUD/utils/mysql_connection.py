
import pymysql.cursors


class MySQLConnection:
    """Clase modelo MySQL connection."""

    def __init__(self, db):

        connection = pymysql.connect(
            host = "localhost",  # Cambiar por el host de la base de datos.
            user = "root",  # Cambiar por el usuario de la base de datos.
            password = "",  # Cambiar por la contraseña de la base de datos.
            db = db,  # Nombre de la base de datos.
            charset = "utf8mb4",  # Codificación de caracteres.
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = True  # Auto commit.
        )
        self.connection = connection
    
    def query_db(self, query, data=None):

        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print(f"Running Query: {query}")
                executable = cursor.execute(query, data)

                if query.lower().find("insert") >= 0:
                    # Si la consulta es un insert, retorna el id del registro insertado.
                    # El resultado de la consulta es el id del registro insertado.
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # Si la consulta es un select, retorna los registros encontrados.
                    # El resultado de la consulta es una lista de diccionarios.
                    result = cursor.fetchall()
                    return result
                else:
                    # Si la consulta es un update o un delete, no retorna nada.
                    self.connection.commit()
            except Exception as e:
                # En caso de que la consulta falle, retorna False.
                print(f"Something went wrong {e}")
                return False
            finally:
                # Cerrar la conexión a la base de datos.
                self.connection.close()


def connectToMySQL(db):

    return MySQLConnection(db)
