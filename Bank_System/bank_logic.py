import random


class Card:

    IIN = '400000'
    cards = {}

    def __init__(self):
        # self.first_name = first_name
        # self.last_name = last_name
        self.account_number = None
        self.card_number = None
        self.pin_code = None
        self.card = None
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
            self.generate_card_number()
            self.generate_pin()
            d = {self.card: self.pin_code}
            for k in d:
                if k not in Card.cards:
                    Card.cards.update(d)
                    return "Account created"

    def get_account_details(self):
        return self.card, self.pin_code

    def view_balance(self):
        ...


# class CardHolder(Card):
#
#     def __init__(self, first_name, last_name):
#         super(CardHolder, self).__init__()
#         self.first_name = first_name
#         self.last_name = last_name
#
#
#     @staticmethod
#     def sequence():
#         num = 0
#         while num < 9999999:
#             yield num
#             num += 1
#
#     acc_number_gen = sequence()




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


# card1 = Card()
# print(card1.create_account())
# print(Card.cards)
# card2 = Card()
# print(card2.create_account())
# print(Card.cards)
