from classes.db import DB


class Seat:

    database = '../data/cinema.db'

    def __init__(self, seat_id):
        self.seat_id = seat_id
        self.db = DB(self.database)

    def get_price(self):
        result = self.db.select('SELECT "price" from "Seat" WHERE "seat_id" = ?', self.seat_id)
        price = result[0][0]
        return price

    def is_free(self):
        result = self.db.select('SELECT "taken" from "Seat" WHERE "seat_id" = ?', self.seat_id)
        free = result[0][0]

        return True if free == 0 else False

    def occupy(self):
        if self.is_free():
            self.db.update('UPDATE "Seat" SET "taken" = ? WHERE "seat_id" = ?', 1, self.seat_id)


if __name__ == '__main__':
    seat = Seat('A1')
    print(seat.is_free())
    print(seat.get_price())
    print(seat.occupy())
    print(seat.is_free())
