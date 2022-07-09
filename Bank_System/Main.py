# import logger
import sys
import bank_logic


# creating menu:
def create_account():
    card = bank_logic.Card()
    card.create_account()
    card, pin = card.get_account_details()
    # пусть пока принты будут, потом логгер посмотрим и прикрутим
    print(f"Your account has been created.\nYour card number is:{card}\nYour pin code is:{pin}")


def log_in():
    card = input("Insert your card number:")
    pin = input("Insert your pin code:")
    if card in bank_logic.Card.cards:
        if bank_logic.Card.cards[card] == pin:
            print("You've successfully logged in")
    else:
        print("Card number or pin code is incorrect")


def balance():
    ...


def log_out():
    print("User logged out")


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
    try:
        ma1n = 0
        while True:
            print("Press key to:")
            for k in menu[ma1n]:
                print(f"{k} - {menu[ma1n][k][1]}")
            choice = int(input())
            menu[ma1n][choice][0]()
            if choice == 2:
                ma1n = 1 if ma1n == 0 else 0
    except ValueError:
        print('Wrong input')


if __name__ == '__main__':
    main()



