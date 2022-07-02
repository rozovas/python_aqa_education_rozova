import sys


class Game:

    def __init__(self, field=None):
        if field is None:
            field = [['_'] * 3, ['_'] * 3, ['_'] * 3]
        self.field = field
        self.x_player = True

    def display_field(self):
        print("---------")
        for row in self.field:
            print(f"| {row[0]} {row[1]} {row[2]} |")
        print("---------")

    @staticmethod
    def define_winner(i):
        if i[0] == i[1] == i[2] == "X":
            return 1  # "X wins"
        elif i[0] == i[1] == i[2] == "0":
            return 2  # "0 wins"
        else:
            return 0  # "Draw"

    def divide_field(self):
        h = self.field  # [list(s[0]), list(s[1]), list([2])]
        v = [[self.field[0][0], self.field[1][0], self.field[2][0]],
             [self.field[0][1], self.field[1][1], self.field[2][1]],
             [self.field[0][2], self.field[1][2], self.field[2][2]]]
        d = [[self.field[0][0], self.field[1][1], self.field[2][2]],
             [self.field[0][2], self.field[1][1], self.field[2][0]]]
        return h, v, d

    def get_winner(self):
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
            return 0

    def accept_coordinates(self, x, y, char):
        x = int(x)
        y = int(y)
        if not (0 < x < 4 and 0 < y < 4):
            raise CellNumberError
            # TODO: rise exception
        elif self.field[x - 1][y - 1] != '_':
            return "The cell is occupied! Choose another one!"
        else:
            if char == 'X':
                if self.get_winner() is None:
                    self.field[x - 1][y - 1] = 'X'
            else:
                if self.get_winner() is None:
                    self.field[x - 1][y - 1] = '0'


class Player:

    # def __new__(cls, **kwargs):
    #     ...

    def __init__(self, name):
        self.name = name
        self.win_log = 0
        # self.age = age

    def __str__(self):
        return self.name

    def win_log_update(self):
        self.win_log += 1
        return self.win_log


class CellNumberError(Exception):

    def __init__(self):
        self.message = "Coordinates should be from 1 to 3"

    def __str__(self):
        return self.message


class CellOccupiedError(Exception):

    def __init__(self):
        self.message = "This cell is occupied."

    def __str__(self):
        return self.message

#
# def another_game():
#     ...


def start_game(player_x, player_0):
    current_player = player_x
    game = Game()
    game.display_field()
    game_finished = 0
    while True:
        try:
            x, y = input(f"{current_player.name}, insert coordinates: ").split()
            # x, y = i[int(el) for el in input("Insert coordinates: ").split()]
            game.accept_coordinates(x, y, 'X' if current_player == player_x else '0')
            current_player = player_x if current_player == player_0 else player_0
            game.display_field()
            winner = game.get_winner()
            if winner is not None:
                if winner == 1:
                    print(f"{player_x.name} wins. Congrats!")
                    return
                elif winner == 2:
                    print(f"{player_0.name} wins. Well done!")
                    return
                elif winner == 0:
                    print("Draw")
                    return
                elif winner == 3:
                    print("Impossible")

        except ValueError:
            print("You should enter two numbers separated by space!")

        except CellNumberError as c:
            print(c)

        except CellOccupiedError as o:
            print(o)


def main():

    def play_game():
        player_x = Player(input("Player X, insert your name: "))
        player_0 = Player(input("Player 0, insert your name: "))
        new_game = True
        while new_game:
            start_game(player_x, player_0)
            another_game = int(input("Insert 1 to play another game, insert any other to get back to main menu"))
            new_game = another_game == 1

    def view_log():
        pass

    def clear_log():
        pass

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
                print(f"{k}. {menu[k][1]}")
            choice = int(input())
            menu[choice][0]()
        except (KeyError, ValueError):
            print("Wrong input.")

    # if menu == 1:
    #     player_x = Player(input("Player X, insert your name: "))
    #     player_0 = Player(input("Player 0, insert your name: "))
    #     play_game(player_x, player_0)


if __name__ == "__main__":
    main()