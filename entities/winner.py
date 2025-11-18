from persistence.db import get_db_connection
class Winner:
    def __init__(self,id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def save(self):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            query = "INSERT INTO winners (name, email) VALUES (%s, %s)"
            cursor.execute(query, (self.name, self.email))
            connection.commit()

            self.id = cursor.lastrowid
            return self.id
        except Exception as ex:
            print("Error al guardar el registro:", ex)
            return 0
        finally:
            cursor.close()
            connection.close()
