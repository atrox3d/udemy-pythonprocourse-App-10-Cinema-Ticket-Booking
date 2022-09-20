import random
import string


class Ticket:

    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.seat_number = seat_number
        self.id = "".join(
            [random.choice(string.ascii_letters) for i in range(8)]
        )

    def to_pdf(self):
        pass
