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
        else:
            if s.count("_") == 0:
                # Draw
                return 0

    def make_move(self, x, y):
        if self.field[x - 1][y - 1] != '_':
            return "The cell is occupied! Choose another one!"
        else:
            if self.x_player:
                self.field[x - 1][y - 1] = 'X'
                self.x_player = False
                return self.get_winner()
            elif not self.x_player:
                self.field[x - 1][y - 1] = '0'
                self.x_player = True
                return self.get_winner()
            self.display_field()
            if self.get_winner() is not None:
                break  # is_playing = False


class Player:

    # def __new__(cls, **kwargs):
    #     ...

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Player: {self.name}\nAge: {self.age}"


def play_game():
    game = Game()
    game.display_field()
    x_player = True
    while True:
        x, y = input("Insert coordinates: ").split()
        # x, y = i[int(el) for el in input("Insert coordinates: ").split()]
        x = int(x)
        y = int(y)
        if s[x - 1][y - 1] != '_':
            print("The cell is occupied! Choose another one!")
        # elif get_winner(h, v, d) == 3:
        #     print("Impossible. Select the other coordinates ")
        else:
            if x_player:
                s[x - 1][y - 1] = 'X'
                x_player = False
                print(get_winner(s))
            elif not x_player:
                s[x - 1][y - 1] = '0'
                print(get_winner(s))
                x_player = True
            display(s)
            if get_winner(s) is not None:
                break  # is_playing = False


play_game()

# s = ['XOX', 'OOX', 'XXO']
# h, v, d = divide(s)
# print(impossible(h, v, d))
