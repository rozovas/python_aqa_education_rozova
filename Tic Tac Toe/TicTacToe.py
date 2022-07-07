import sys
import logging

# creating a custom logger:
logger = logging.getLogger('TicTacToe')


def setup_logger():
    # creating and managing handlers:
    f_handler = logging.FileHandler('game.log')
    # stream=sys.stdout added to prevent the issue of PyCharm:
    # https://youtrack.jetbrains.com/issue/IDEA-70016/error-mixing-stdoutstderr
    s_handler = logging.StreamHandler(stream=sys.stdout)
    f_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s'))
    s_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s: %(message)s'))

    class WinnersOnly(logging.Filter):
        """filtering only records about winners to file"""
        def filter(self, record):
            return record.getMessage().endswith('won.')

    f_handler.addFilter(WinnersOnly())
    # adding handlers to a logger:
    logger.addHandler(f_handler)
    logger.addHandler(s_handler)

    # setting levels:
    logger.setLevel(logging.DEBUG)
    f_handler.setLevel(logging.INFO)
    s_handler.setLevel(logging.INFO)

    # function to test logger:
    def test_log():
        print("==========================")
        print("Unit test 1. Тестируем лог")
        print("==========================")
        logger.debug("DEBUG LOG")
        logger.info("INFO LOG")
        logger.warning("WARNING LOG")
        logger.error("ERROR LOG")
        logger.critical("CRITICAL LOG")
        # Этот вывод должен попасть в файл
        logger.critical("John Cena wins. Congrats!")
        print("==========================")
        print("Unit test 1. Тест окончен")
        print("==========================\n")

    # test_log()


class CellNumberError(Exception):

    def __init__(self):
        self.message = "Coordinates should be from 1 to 3"

    def __str__(self):
        return self.message


class CellOccupiedError(Exception):

    def __init__(self, message="This cell is occupied."):
        self.message = message

    def __str__(self):
        return self.message


class PlayerExists(Exception):

    def __init__(self, message="Player with such name already exists"):
        self.message = message

    def __str__(self):
        return self.message


class Game:
    """Class containing main game logic"""

    def __init__(self, field=None):
        if field is None:
            field = [['_'] * 3, ['_'] * 3, ['_'] * 3]
        self.field = field
        self.x_player = True

    def display_field(self):
        """Returns current field state that can be printed"""

        def mutable_part():
            f2 = []
            for row in self.field:
                f1 = f"| {row[0]} {row[1]} {row[2]} |\n"
                f2.append(f1)
            return f2[0] + f2[1] + f2[2]

        frame = "_________\n"
        return frame + mutable_part() + frame

    @staticmethod
    def define_winner(i):
        """Defines winner taking a row of 3 characters as argument"""
        if i[0] == i[1] == i[2] == "X":
            return 1  # "X wins"
        elif i[0] == i[1] == i[2] == "0":
            return 2  # "0 wins"
        else:
            return 0  # "Draw"

    def divide_field(self):
        """Divides current field into rows from a direction point of view: horizontal, vertical, diagonal
        which helps in further field manipulations and calculations"""
        h = self.field  # [list(s[0]), list(s[1]), list([2])]
        v = [[self.field[0][0], self.field[1][0], self.field[2][0]],
             [self.field[0][1], self.field[1][1], self.field[2][1]],
             [self.field[0][2], self.field[1][2], self.field[2][2]]]
        d = [[self.field[0][0], self.field[1][1], self.field[2][2]],
             [self.field[0][2], self.field[1][1], self.field[2][0]]]
        return h, v, d

    def get_winner(self):
        """Determines if somebody won depending on the current state of the field"""
        h, v, d = self.divide_field()
        l = []
        x = h[0].count('X') + h[1].count('X') + h[2].count('X')
        o = h[0].count('0') + h[1].count('0') + h[2].count('0')

        for i in [*h, *v, *d]:
            l.append(self.define_winner(i))
        if (l.count(1) >= 1 and l.count(2) >= 1) or (abs(x - o) > 1):
            # Impossible
            return 3
        elif l.count(1) == 1:
            # X wins
            return 1
        elif l.count(2) == 1:
            # 0 wins
            return 2
        elif "_" in [*self.field]:
            # Draw
            # TODO: think if Draw can be determined in some other way
            return 0

    def accept_coordinates(self, x, y, char):
        """Accepts coordinates and the character of the player (supposed to be X or 0),
        checks if the cell is not yet occupied, and if there is no winner yet, changes the field accordingly"""
        x = int(x)
        y = int(y)
        if not (0 < x < 4 and 0 < y < 4):
            raise CellNumberError()
        elif self.field[x - 1][y - 1] != '_':
            raise CellOccupiedError
        else:
            if self.get_winner() is None:
                if char == 'X':
                    self.field[x - 1][y - 1] = 'X'
                elif char == '0':
                    self.field[x - 1][y - 1] = '0'


class Player:
    """Used to create a player for a game. Has the only attribute of name"""

    def __init__(self, name):
        self.name = name
        # self.win_log = 0

    def __str__(self):
        return self.name

    # def win_log_update(self):
    #     self.win_log += 1
    #     return self.win_log


# client part


def game_time(func):
    """decorator that allows to calculate and log time spent for one game session"""
    import time

    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        t = round(end - start)
        logger.info(f"Game lasted for {t} seconds")

    return wrapper


@game_time
def start_game(player_x, player_0):
    """Accepts two players and performs the game until one player wins, or it's draw"""
    current_player = player_x
    game = Game()
    print(game.display_field())
    while True:
        try:
            x, y = input(f"{current_player}, insert coordinates: ").split()
            # x, y = i[int(el) for el in input("Insert coordinates: ").split()]
            game.accept_coordinates(x, y, 'X' if current_player == player_x else '0')
            current_player = player_x if current_player == player_0 else player_0
            print(game.display_field())
            winner = game.get_winner()
            if winner == 1:
                logger.info(f"{player_x.name} won.")
                return
            elif winner == 2:
                logger.info(f"{player_0.name} won.")
                return
            elif winner == 0:
                logger.info("Draw")
                return
            elif winner == 3:
                logger.info("Impossible")

        except ValueError:
            logger.error("You should enter two numbers separated by space!")

        except CellNumberError as c:
            logger.error(c)

        except CellOccupiedError as o:
            logger.error(o)


def main():
    def play_game():
        player_x_name = player_0_name = True
        while player_x_name == player_0_name:
            player_x_name = input("Player X, insert your name: ")
            player_0_name = input("Player 0, insert your name: ")
            if player_0_name == player_x_name:
                logger.error("Player with such name already exists. Choose another name")
        player_x = Player(player_x_name)
        player_0 = Player(player_0_name)
        new_game = True
        while new_game:
            start_game(player_x, player_0)
            another_game = input("Insert 1 to play another game, insert any other to get back to main menu")
            new_game = another_game == "1"

    def view_log():
        f = open("game.log", mode='r', encoding='utf-8')
        if f.read(1) == '':
            logger.info("The log is empty.")
        else:
            print(f.read())
        f.close()

    def clear_log():
        with open("game.log", 'w', encoding='utf-8') as f:
            f.write("")
            f.close()
            logger.info("The log has been cleared")

    def exit_game():
        sys.exit()

    menu = {
        1: (play_game, "Play a new game"),
        2: (view_log, "View log"),
        3: (clear_log, "Clear log"),
        4: (exit_game, "Exit")
    }

    while True:
        try:
            print("Press key to:")
            for k in menu:
                print(f"{k} - {menu[k][1]}")
            choice = int(input())
            menu[choice][0]()
        except (KeyError, ValueError):
            logger.error("Wrong input.")
        except FileNotFoundError:
            logger.error("The log is empty")
        except Exception as e:
            logger.error(e)


if __name__ == '__main__':
    setup_logger()
    main()