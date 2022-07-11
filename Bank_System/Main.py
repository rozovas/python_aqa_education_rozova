import logger
import sys
from bank_logic import Bank
from bank_logic import IncorrectCardOrPin, IncorrectFormat
from input_handler import InputHandler


# CLASS TO ENCLOSE BANK APP VARIABLES
class App:
    my_bank = Bank('Lana Bank', 400000)
    input_handler = InputHandler()
    # change to False to disable test mode
    input_handler.test_mode = False
    logged_in = Bank.UNAUTHORIZED
    current_card = None
    current_pin = None


# MENU FUNCTIONS
def create_account():
    App.current_card, App.current_pin = App.my_bank.create_account()
    # logger.bank_logger.info(l_bank.info["created"])
    # logger.bank_logger.info\
    print(f"Your card number is:\n{App.current_card}\n"
          f"Your pin code is: \n{App.current_pin}")


def log_in():
    while App.logged_in == Bank.UNAUTHORIZED:
        try:
            App.current_card = App.input_handler.h_input(InputHandler.messages['card'])
            App.current_pin = App.input_handler.h_input(InputHandler.messages['pin'])
            App.logged_in = App.my_bank.log_in(App.current_card, App.current_pin)
            if App.logged_in == Bank.AUTHORIZED:
                logger.bank_logger.info(App.my_bank.get_message('authorized'))
                return
            else:
                logger.bank_logger.info(App.my_bank.get_message('unauthorized'))
                return
        except IncorrectFormat as i:
            logger.bank_logger.error(i)
        except IncorrectCardOrPin as e:
            logger.bank_logger.error(e)


def balance():
    logger.bank_logger.info(f"Your current balance is {App.my_bank.view_balance(App.current_card)}")


def log_out():
    App.my_bank.log_out(App.current_card)
    App.logged_in = Bank.UNAUTHORIZED
    logger.bank_logger.info('logged out')


def ex1t():
    sys.exit()


# MENU ITEMS
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


# MAIN FUNCTION
def main_decorator_for_test_mode(func):
    choice = None
    if App.input_handler.test_mode:
        test_obj = App.my_bank.get_card_obj()
        App.input_handler.update_test_object(test_obj)
    if not App.input_handler.test_mode:
        return func()

    def wrapper():
        while True:
            try:
                for k in menu[App.logged_in]:
                    print(f"{k} - {menu[App.logged_in][k][1]}")
                test_choice = App.input_handler.test_choice
                menu[App.logged_in][test_choice][0]()
            except (ValueError, KeyError):
                logger.bank_logger.error("Wrong input")
            except IncorrectFormat as i:
                logger.bank_logger.error(i)
            except IncorrectCardOrPin as i:
                logger.bank_logger.error(i)

    return wrapper()


# remove decorator when done testing
@main_decorator_for_test_mode
def main():
    while True:
        try:
            print("Menu:")
            for k in menu[App.logged_in]:
                print(f"{k} - {menu[App.logged_in][k][1]}")
            choice = int(App.input_handler.h_input(InputHandler.messages['menu']))
            menu[App.logged_in][choice][0]()
        # except (ValueError, KeyError):
        #     logger.bank_logger.error("Wrong input")
        except IncorrectFormat as i:
            logger.bank_logger.error(i)
        except IncorrectCardOrPin as i:
            logger.bank_logger.error(i)


# FUNCTION FOR TESTING

# if True, test_mode is enabled, allows to avoid entering the card manually, gets random card and its pin


# def test(func):
#     while test_mode:


if __name__ == '__main__':
    logger.setup_logger()
    main()

