import sqlite3


class DB:
    
    def __init__(self, path):
        self.path = path

    def select(self, query, *params):
        connection = sqlite3.connect(self.path)
        cursor = connection.cursor()
        # print(f'DB.select | query: {query} | params: {params}')
        cursor.execute(query, params)
        return cursor.fetchall()
