from classes.db import DB


class Card:

    database = '../data/banking.db'

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder
        self.db = DB(self.database)

    def validate(self, price):
        result = self.db.select('SELECT "balance" from "Card" WHERE "number" = ? and "cvc" = ?', self.number, self.cvc)
        if result:
            balance = result[0][0]
            if balance >= price:
                self.db.update('UPDATE "Card" SET "balance" = ? WHERE "number" = ? and "cvc" = ?', balance - price, self.number, self.cvc)
                return True


if __name__ == '__main__':
    card = Card('Visa', '12345678', '123', 'John Smith')
    card.validate(4400)