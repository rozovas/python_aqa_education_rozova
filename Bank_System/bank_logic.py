import random


class BankSystem:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def sequence():
        num = 0
        while num < 9999999:
            yield num
            num += 1

    acc_number_gen = sequence()


class Card:

    IIN = '400000'
    cards = {}

    def __init__(self, card, pin_code):
        # self.first_name = first_name
        # self.last_name = last_name
        self.account_number = None
        self.card_number = None
        self.pin_code = pin_code
        self.card = card
        self.balance = 0

    @staticmethod
    def generate_random_num(length):
        length = int(length)
        num = ''
        for i in range(length):
            n = str(random.randint(0, 9))
            num += n
        return num

    def generate_account_number(self):
        number = self.generate_random_num(8)
        self.account_number = number

    def generate_pin(self):
        pin = self.generate_random_num(4)
        self.pin_code = pin

    def generate_card_number(self):
        self.generate_account_number()
        self.card = Card.IIN + self.account_number

    def create_account(self):
        while True:
            # self.generate_card_number()
            # self.generate_pin()
            d = {self.card: self.pin_code}
            for k, v in d.items():
                if k not in Card.cards and v not in Card.cards:
                    Card.cards.update(d)
                    return "Account created"
                else:
                    self.card = input("Insert another number")




# test

# john = CardHolder('John', 'Mitchell')
# john.generate_account_number()
# john.generate_pin()
# john.generate_random_num(5)
# print(john.account_number)
# print(john.pin_code)

# bank = BankSystem('Privat')
# for i in range(5):
#     print(next(bank.acc_number_gen))


card1 = Card(card='01234567890', pin_code='1234')
print(card1.create_account())
print(Card.cards)
card2 = Card(card='01234567890', pin_code='1234')
print(card2.create_account())
print(Card.cards)
