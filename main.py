from classes.user import User
from classes.seat import Seat
from classes.card import Card

username = input('your full name: ')
seat_id = input('preferred seat number: ')
card_type = input('your card type: ')
card_number = input('your card number: ')
card_cvc = input('your card cvc: ')
card_holder = input('card holder name: ')

user = User(username)
seat = Seat(seat_id)
card = Card(card_type, card_number, card_cvc, card_holder)

print(user.buy(seat, card))
