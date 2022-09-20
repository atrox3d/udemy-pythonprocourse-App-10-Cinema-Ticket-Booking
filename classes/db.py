import sqlite3


class DB:
    
    def __init__(self, path):
        self.path = path

    def select(self, query, *params):
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        connection.close()
        return result

    def update(self, query, *params):
        connection = sqlite3.connect(self.path)
        connection.execute(query, params)
        connection.commit()
        connection.close()

