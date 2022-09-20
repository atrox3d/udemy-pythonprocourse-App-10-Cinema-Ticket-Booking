import sqlite3


class Seat:

    database = 'cinema.db'

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "price" from "Seat" WHERE "seat_id" = ?
        """, [self.seat_id])
        result = cursor.fetchall()
        price = result[0][0]
        return price

    def is_free(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" from "Seat" WHERE "seat_id" = ?
        """, [self.seat_id])
        result = cursor.fetchall()
        free = result[0][0]

        return True if free == 0 else False

    def occupy(self):
        pass


if __name__ == '__main__':
    seat = Seat('A1')
    print(seat.is_free())
    print(seat.get_price())
