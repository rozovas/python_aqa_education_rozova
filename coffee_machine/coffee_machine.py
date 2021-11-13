import sys
import enum


class CoffeeMachine:
    """
    Coffee machine simulator.
    """

    class States(enum.Enum):
        MENU = 1
        CHOOSE_COFFEE = 2
        REFILL_W = 3
        REFILL_C = 4
        REFILL_M = 5
        REFILL_CUPS = 6
        GIVING_MONEY = 7
        PRINTING_REMAINING = 8

    START = 'Insert action you\'d like to do: \nbuy \nfill \ntake \nremaining \nexit'


    def coffee_recipe(w=0, c=0, m=0):
        """Makes coffee recipe
        :param w: amount of water
        :param c: amount of coffee
        :param m: amount of milk
        :return: dictionary with necessary ingredients for a certain coffee recipe
        """
        return {'water': w,
                'coffee': c,
                'milk': m
                }

    RECIPES = {
            'latte': coffee_recipe(350, 20, 75),
            'espresso': coffee_recipe(250, 16),
            'cappuccino': coffee_recipe(200, 12, 100)
        }

    def __init__(self, money=0, cups=0, water=0, milk=0, coffee=0):
        """Initialiaes coffee machine.
        :param money: initial amount of money.
        :param cups: initial amount of cups.
        :param water: initial amount of water.
        :param milk: initial amount of milk.
        :param coffee: initial amount of coffee.
        """
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money
        self.prices = {'latte': 7, 'cappuccino': 6, 'espresso': 4}
        self.state = CoffeeMachine.States.MENU

    def set_state(self, state):
        self.state = state

    def take_money(self):
        m = self.money
        self.money = 0
        return f'I gave you {m}\n'

    def print_remaining(self):
        return f'''The coffee machine has: 
                {self.water} ml of water 
                {self.milk} ml of milk 
                {self.coffee} g of coffee beans 
                {self.cups} disposable cups 
                {self.money} of money
                '''

    def make_coffee(self, coffee_type: str):
        """Tries to make coffee.
        :param coffee_type: can be 'latte', 'espresso' or 'cappuccino'.
        Checks if there are enough resources for making a cup of the selected type of coffee.
        Tops up coffee machine money balance. Subtracts resources.
        """
        r = CoffeeMachine.RECIPES[coffee_type]
        w = r['water']
        c = r['coffee']
        m = r['milk']
        can_make = 1
        if self.water < w:
            can_make = 'Sorry, not enough water!' + '\n' + CoffeeMachine.START
        if self.coffee < c:
            can_make = 'Sorry, not enough coffee!' + '\n' + CoffeeMachine.START
        if self.milk < m:
            can_make = 'Sorry, not enough milk!' + '\n' + CoffeeMachine.START
        if self.cups < 1:
            can_make = 'Sorry, not enough cups!' + '\n' + CoffeeMachine.START
        if can_make != 1:
            self.set_state(CoffeeMachine.States.MENU)
            return can_make

        self.money += self.prices[coffee_type]
        self.coffee -= CoffeeMachine.RECIPES[coffee_type]['coffee']
        self.milk -= CoffeeMachine.RECIPES[coffee_type]['milk']
        self.water -= CoffeeMachine.RECIPES[coffee_type]['water']
        self.cups -= 1
        self.set_state(CoffeeMachine.States.MENU)
        return f'I have enough resources, making you a cup of {coffee_type}!' + '\n' + CoffeeMachine.START

    def process(self, input_str):
        """Processes user string input.
        :param input_str: input string.
        Main coffee machine method.
        It processes user input and executes actions depending on the current coffee machine state.
        """
        if self.state == CoffeeMachine.States.MENU:
            if input_str == 'buy':
                self.set_state(CoffeeMachine.States.CHOOSE_COFFEE)
                return 'For espresso insert "1", ' \
                       'for latte insert "2", ' \
                       'for cappuccino insert "3", ' \
                       '"back" - to main menu.'
            if input_str == 'fill':
                self.set_state(CoffeeMachine.States.REFILL_W)
                return 'Water amount'
            if input_str == 'take':
                return self.take_money() + '\n' + CoffeeMachine.START
            if input_str == 'remaining':
                return self.print_remaining() + '\n' + CoffeeMachine.START
            if input_str == 'exit':
                sys.exit()
            return CoffeeMachine.START

        elif self.state == CoffeeMachine.States.CHOOSE_COFFEE:
            if input_str == '1':
                return self.make_coffee('espresso')
            elif input_str == '2':
                return self.make_coffee('latte')
            elif input_str == '3':
                return self.make_coffee('cappuccino')
            elif input_str == 'back':
                pass
            self.set_state(CoffeeMachine.States.MENU)
            return CoffeeMachine.START

        elif self.state == CoffeeMachine.States.REFILL_W:
            self.water += int(input_str)
            self.set_state(CoffeeMachine.States.REFILL_C)
            return 'Coffee amount:'

        elif self.state == CoffeeMachine.States.REFILL_C:
            self.coffee += int(input_str)
            self.set_state(CoffeeMachine.States.REFILL_M)
            return 'Milk amount:'

        elif self.state == CoffeeMachine.States.REFILL_M:
            self.milk += int(input_str)
            self.set_state(CoffeeMachine.States.REFILL_CUPS)
            return 'Cups amount:'

        elif self.state == CoffeeMachine.States.REFILL_CUPS:
            self.cups += int(input_str)
            self.set_state(CoffeeMachine.States.MENU)
            return CoffeeMachine.START


coffee_machine = CoffeeMachine(550, 9, 400, 540, 120)
action = ''
while True:
    print(coffee_machine.process(action))
    action = input()
