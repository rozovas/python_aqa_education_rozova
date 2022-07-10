import logger
import sys
import bank_logic
from bank_logic import IncorrectCardOrPin


class IncorrectFormat(Exception):

    def __init__(self, message="The inserted card number or pin code does not correspond to required format."
                               "Card number length should be 12 digits, pin code length - 4 digits"):
        self.message = message

    def __str__(self):
        return self.message


l_bank = bank_logic.Bank('Lana Bank', '400000')
logged_in = 0
current_card = None
current_pin = None


# creating menu:
def create_account():
    global current_card, current_pin
    current_card, current_pin = l_bank.create_account()
    # logger.bank_logger.info(l_bank.info["created"])
    # logger.bank_logger.info\
    print(f"Your card number is:\n{current_card}\n"
                       f"Your pin code is: \n{current_pin}")


def log_in():
    global logged_in
    global current_card, current_pin
    while logged_in == 0:
        try:
            current_card = input("Insert your card number")
            if 'q' == current_card:
                return
            elif len(current_card) != 14:
                raise IncorrectFormat
            else:
                current_pin = input("Insert your card number")
                if current_pin == 'q':
                    return
                logged_in = l_bank.log_in(current_card, current_pin)
                if logged_in == 1:
                    logger.bank_logger.info(l_bank.get_message('authorized'))
                    return
                else:
                    logger.bank_logger.info(l_bank.get_message("unauthorized"))
                    return
        except IncorrectFormat as i:
            logger.bank_logger.error(i)
        except IncorrectCardOrPin as e:
            logger.bank_logger.error(e)


def balance():
    global current_card
    logger.bank_logger.info(f"Your current balance is {l_bank.view_balance(current_card)}")


def log_out():
    global current_card
    global logged_in
    l_bank.log_out(current_card)
    logged_in = 0
    logger.bank_logger.info('logged out')


def ex1t():
    sys.exit()


main_menu = {
    1: (create_account, "Create account"),
    2: (log_in, "Log in"),
    3: (ex1t, "Exit")
}

user_menu = {
    1: (balance, "Balance"),
    2: (log_out, "Log out"),
    3: (ex1t, "Exit")
}

menu = [main_menu, user_menu]


def main():
    global ma1n
    while True:
        try:
            print("Press key to:")
            for k in menu[logged_in]:
                print(f"{k} - {menu[logged_in][k][1]}")
            choice = int(input())
            menu[logged_in][choice][0]()
        except ValueError:
            logger.bank_logger.error('Wrong input')


def test():
    ...


if __name__ == '__main__':
    logger.setup_logger()
    main()