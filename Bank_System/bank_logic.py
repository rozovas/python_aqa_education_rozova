import random


# CLASSES TO MANAGE EXCEPTIONS
class IncorrectCardOrPin(Exception):

    def __init__(self, message='The inserted card number or pin code is incorrect'):
        self.message = message

    def __str__(self):
        return self.message


class IncorrectFormat(Exception):

    def __init__(self, message="The inserted card number or pin code does not correspond to required format."
                               "Card number length should be 12 digits, pin code length - 4 digits"):
        self.message = message

    def __str__(self):
        return self.message


# BANK LOGIC: CLASSES AND FUNCTIONS
def generate_random_num(length):
    length = int(length)
    num = ''
    for i in range(length):
        n = str(random.randint(0, 9))
        num += n
    return num


class Card:
    cards = []
    pin_length = 4

    def __init__(self, iin: int, c_length: int):
        # self.first_name = first_name
        # self.last_name = last_name
        self.account_number = None
        self.card_number = None
        self.pin_code = None
        self.balance = 0
        self.iin = iin
        self.c_length = c_length
        self.a_length = None
        self.p_length = Card.pin_length

    def generate_account_number(self):
        self.a_length = self.c_length - len(str(self.iin))
        self.account_number = generate_random_num(self.a_length)

    def generate_pin(self):
        self.pin_code = generate_random_num(self.p_length)

    def generate_card_number(self):
        self.generate_account_number()
        self.card_number = str(self.iin) + self.account_number


class Bank:
    card_length = 14
    accounts = {}
    acc_number = 0
    info = {"created": f"Your account has been created. ",
            "authorized": "You've successfully logged in.",
            "unauthorized": "The inserted card number or pin code is incorrect."}

    AUTHORIZED = 1
    UNAUTHORIZED = 0

    def __init__(self, name, iin):
        self.name = name
        self.iin = iin

    @staticmethod
    def get_message(m: 'created, authorized, unauthorized'):
        return Bank.info[m]

    def create_account(self):
        card = Card(self.iin, self.card_length)
        card.generate_card_number()
        card.generate_pin()
        if card.card_number not in Bank.accounts:
            Bank.accounts.update({card.card_number: {"pin_code": card.pin_code,
                                                     "account_number": card.account_number,
                                                     "balance": card.balance,
                                                     "status": Bank.UNAUTHORIZED,
                                                     "obj": card}})
            Bank.acc_number += 1
            return card.card_number, card.pin_code

    @staticmethod
    def log_in(card_number, pin_code):
        for c in Bank.accounts:
            if card_number == c:
                if pin_code == Bank.accounts[c]['pin_code']:
                    Bank.accounts[c]["status"] = Bank.AUTHORIZED
                    return Bank.accounts[c]["status"]
            else:
                raise IncorrectCardOrPin

    @staticmethod
    def view_balance(card_number):
        for c in Bank.accounts:
            if card_number in Bank.accounts[c]:
                return Bank.accounts[c]["balance"]

    @staticmethod
    def log_out(card_number):
        for c in Bank.accounts:
            if Bank.accounts[c] == card_number:
                Bank.accounts[c]["status"] = Bank.UNAUTHORIZED

    @classmethod  # for testing
    def get_card_obj(cls):
        l = []
        if Bank.acc_number > 0:
            for c in Bank.accounts:
                l.append(Bank.accounts[c]['obj'])
            return l[random.randint(0, Bank.acc_number - 1)]
        else:
            return Bank.acc_number

# SOME TESTING
# bank = Bank('b', 400000)
# bank.create_account()
# bank.create_account()
# print(bank.accounts)
# print(Bank.)
