from classes.seat import Seat
from classes.card import Card
from classes.ticket import Ticket


class User:

    def __init__(self, name):
        self.name = name

    def buy(self, seat: Seat, card: Card):
        if seat.is_free():
            price = seat.get_price()
            if card.validate(price):
                seat.occupy()
                ticket = Ticket(self, price, seat.seat_id)
                ticket.to_pdf()
                return "Purchase succesful!"
            else:
                return "There was a problem with your card!"
        else:
            return "Seat is taken"

