import sqlite3


class Card:

    database = 'data/banking.db'

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "balance" from "Card" WHERE "number" = ? and "cvc" = ?
        """, [self.number, self.cvc])
        result = cursor.fetchall()

        if result:
            balance = result[0][0]
            if balance >= price:
                connection.execute("""
                UPDATE "Card" SET "balance" = ? WHERE "number" = ? and "cvc" = ?
                """, [balance - price, self.number, self.cvc])
                connection.commit()
                connection.close()
                return True
