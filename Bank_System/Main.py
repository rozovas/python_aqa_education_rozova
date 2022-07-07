import logger
import sys
# creating menu:


def create_account():
    print('Account_created')


def log_in():
    print("Successful login")


def balance():
    print("You have some money")


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


def print_menu():
    try:
        main = 0
        while True:
            print("Press key to:")
            for k in menu[main]:
                print(f"{k} - {menu[main][k][1]}")
            choice = int(input())
            menu[main][choice][0]()
            if choice == 2:
                main = 1 if main == 0 else 0
    except ValueError:
        logger.logger.error('Wrong input')


if __name__ == '__main__':
    print_menu()



