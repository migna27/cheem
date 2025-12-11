from persistence.db import get_db_connection
class Winner:
    def __init__(self,id, name, email, phrase, creado=None, intentos=1):
        self.id = id
        self.name = name
        self.email = email
        self.phrase = phrase
        self.creado = creado
        self.intentos = intentos

    def save(self):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            query = "INSERT INTO winners (name, email, phrase, intentos) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (self.name, self.email, self.phrase, self.intentos))
            connection.commit()

            self.id = cursor.lastrowid
            return self.id
        except Exception as ex:
            print("Error al guardar el registro:", ex)
            return 0
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def get_all(cls):
        winners = []
        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            query = "SELECT id, name, email, phrase, intentos, creado FROM winners ORDER BY intentos ASC, creado DESC"
            cursor.execute(query)
            results = cursor.fetchall()

            for row in results:
                winner = cls(id=row[0], name=row[1], email=row[2], phrase=row[3], intentos=row[4], creado=row[5])
                winners.append(winner)
            return winners
        except Exception as ex:
            print("Error al obtener los registros:", ex)
            return []
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def delete(cls, id):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            
            query = "DELETE FROM winners WHERE id = %s"
            cursor.execute(query, (id,))
            connection.commit()
            return True
            
        except Exception as ex:
            print("Error al eliminar:", ex)
            return False
        finally:
            if 'cursor' in locals() and cursor: cursor.close()
            if 'connection' in locals() and connection: connection.close()

    
        