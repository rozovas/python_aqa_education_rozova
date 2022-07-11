from bank_logic import Bank, Card, IncorrectFormat


class InputHandler:
    messages = {'card': "Insert your card number: ",
                'pin': "Insert your pin code: ",
                'menu': "Select option: "
                }

    def __init__(self, test_object=None):
        self.test_mode = False
        self.test_menu = 0
        self.test_choice = 1
        self.test_object = test_object

    # @classmethod
    # def add_message(cls, m_name, m_text):
    #     InputHandler.messages.update({m_name: m_text})

    def update_test_object(self, test_obj):
        self.test_mode = test_obj

    @staticmethod
    def quit_input_validator(my_input: str):
        back_to_menu = 'q'
        if my_input == back_to_menu:
            return
        else:
            return my_input

    @staticmethod
    def is_digits_validator(my_input: str):
        if my_input.isnumeric():
            return my_input
        else:
            raise IncorrectFormat

    @staticmethod
    def card_validator(my_input):
        if InputHandler.quit_input_validator(my_input) == my_input:
            if InputHandler.is_digits_validator(my_input) == my_input:
                if my_input == Bank.card_length:
                    return my_input
        else:
            raise IncorrectFormat

    @staticmethod
    def pin_validator(my_input):
        if InputHandler.quit_input_validator(my_input) == my_input:
            if InputHandler.is_digits_validator(my_input) == my_input:
                if my_input == Card.pin_length:
                    return my_input
        else:
            raise IncorrectFormat

    @staticmethod
    def menu_item_validator(my_input):
        if len(InputHandler.is_digits_validator(my_input)) == 1:
            if my_input == 1 or my_input == 2 or my_input == 3:
                return my_input

    def change_test_choice(self):
        if self.test_choice == 1:
            self.test_choice = 2
        if self.test_choice == 2:
            self.test_choice = 1

    def h_input(self, mes=None):
        data = {'card': [0 if not self.test_mode else self.test_object.card_number, InputHandler.card_validator],
                'pin': [0 if not self.test_mode else self.test_object.pin_code, InputHandler.pin_validator],
                'menu': [self.test_choice, InputHandler.menu_item_validator]
                }
        if self.test_mode:
            self.change_test_choice()
        if mes in InputHandler.messages:
            for k in data:
                if mes == InputHandler.messages[data[k]]:
                    my_input = input(InputHandler.messages[data[k]])
                    inp = data[k][0] if self.test_mode else data[k][1](my_input)
                    return inp
        else:
            return input(mes)
