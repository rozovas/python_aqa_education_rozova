# import abs from math

def divide(s):
    h = s  # [list(s[0]), list(s[1]), list([2])]
    v = [[s[0][0], s[1][0], s[2][0]],
         [s[0][1], s[1][1], s[2][1]],
         [s[0][2], s[1][2], s[2][2]]]
    d = [[s[0][0], s[1][1], s[2][2]],
         [s[0][2], s[1][1], s[2][0]]]
    return h, v, d


def display(h):
    print("---------")
    for row in h:
        print(f"| {row[0]} {row[1]} {row[2]} |")
    print("---------")


def define_winner(i):
    if i[0] == i[1] == i[2] == "X":
        return 1  # "X wins"
    elif i[0] == i[1] == i[2] == "0":
        return 2  # "0 wins"
    else:
        return 3  # "Draw"


def get_winner(h, v, d):
    l = []
    x = h[0].count('X') + h[1].count('X') + h[2].count('X')
    o = h[0].count('0') + h[1].count('0') + h[2].count('0')
    for i in [*h, *v, *d]:
        l.append(define_winner(i))
    if (l.count(1) >= 1 and l.count(2) >= 1) or (abs(x - o) > 1):
        return 0
    elif l.count(1) == 1:
        return 1
    elif l.count(2) == 1:
        return 2
    else:
        return 3


def play_game():
    s = [['_'] * 3, ['_'] * 3, ['_'] * 3]
    display(s)
    while True:
        x, y = input("Insert coordinates: ").split()
        # x, y = i[int(el) for el in input("Insert coordinates: ").split()]
        x = int(x)
        y = int(y)
        h, v, d = divide(s)
        if s[x-1][y-1] != '_':
            print("The cell is occupied! Choose another one!")
        elif get_winner(h, v, d) == 3:
            print("Impossible. Select the other coordinates ")
        else:
            s[x-1][y-1] = 'X'
                if get_winner()
            elif get_winner(h, v, d) ==
            display(s)


play_game()


# s = ['XOX', 'OOX', 'XXO']
# h, v, d = divide(s)
# print(impossible(h, v, d))
