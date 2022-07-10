import random


def generate_random_num(length):
    length = int(length)
    num = ''
    for i in range(length):
        n = str(random.randint(0, 9))
        num += n
    return num


class IncorrectCardOrPin(Exception):

    def __init__(self, message='The inserted card number or pin code is incorrect'):
        self.message = message

    def __str__(self):
        return self.message


class Card:

    def __init__(self, iin):
        # self.first_name = first_name
        # self.last_name = last_name
        self.account_number = None
        self.card_number = None
        self.pin_code = None
        self.balance = 0
        self.iin = iin

    def generate_account_number(self):
        number = generate_random_num(8)
        self.account_number = number

    def generate_card_number(self):
        self.generate_account_number()
        self.card_number = self.iin + self.account_number

    def generate_pin(self):
        pin = generate_random_num(4)
        self.pin_code = pin


class Bank:

    accounts = {}
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

    # @staticmethod
    def create_account(self):
        card = Card(self.iin)
        card.generate_card_number()
        card.generate_pin()
        if card.card_number not in Bank.accounts:
            Bank.accounts.update({card: {"card_number": card.card_number,
                                         "pin_code": card.pin_code,
                                         "account_number": card.account_number,
                                         "balance": card.balance,
                                         "status": Bank.UNAUTHORIZED}})
            return card.card_number, card.pin_code

    @staticmethod
    def log_in(card_number, pin_code):
        for k in Bank.accounts:
            if card_number == Bank.accounts[k]['card_number']:
                if pin_code == Bank.accounts[k]['pin_code']:
                    Bank.accounts[k]["status"] = Bank.AUTHORIZED
                    return Bank.accounts[k]["status"]
            else:
                raise IncorrectCardOrPin

    @staticmethod
    def view_balance(card_number):
        for k in Bank.accounts:
            if card_number in Bank.accounts[k]["card_number"]:
                return Bank.accounts[k]["balance"]

    @staticmethod
    def log_out(card_number):
        for k in Bank.accounts:
            if Bank.accounts[k]["card_number"] == card_number:
                Bank.accounts[k]["status"] = Bank.UNAUTHORIZED

