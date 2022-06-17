# import abs from math

def divide(s):
    s = s.upper()
    if len(s) == 9:
        h = [list(s[:3]), list(s[3:6]), list(s[6:])]
        v = [[s[0], s[3], s[6]], [s[1], s[4], s[7]], [s[2], s[5], s[8]]]
        d = [[s[0], s[4], s[8]], [s[2], s[4], s[6]]]
    else:
        return "Incorrect string. Insert a 9-long string including '0' (zero) or 'X'"
    return h, v, d


def display(h):
    # print("---------\n")
    # i = 0
    # for i in range(len(h)):
    #     print(f"\n| {h[i][0]} {h[i][1]} {h[i][2]} |")
    #     i += 1
    # print("---------")
    print("---------")
    print(f"| {h[0][0]} {h[0][1]} {h[0][2]} |\n| {h[1][0]} {h[1][1]} {h[1][2]} | \n| {h[2][0]} {h[2][1]} {h[2][2]} |")
    # print(f"| {h[1][0]} {h[1][1]} {h[1][2]} |\n")
    # print(f"| {h[2][0]} {h[2][1]} {h[2][2]} |")
    print("---------\n")


def define_winner(*args):
    for i in args:
        if len(i) == 3:
            if i[0] == i[1] == i[2] == "X":
                return 1  # "X wins"
            elif i[0] == i[1] == i[2] == "0":
                return 2  # "0 wins"
        elif len(i) == 2:
            if i[0] == i[1] == "X":
                return 1  # "X wins"
            elif i[0] == i[1] == "0":
                return 2  # "0 wins"
        else:
            return 0  # "Draw"


def impossible(h, v):

    l = []
    x = h[0].count('X') + h[1].count('X') + h[2].count('X')
    o = h[0].count('0') + h[1].count('0') + h[2].count('0')
    i = 0
    for i in range(len(h)):
        # for j in i:
        l.append(define_winner(h[i]))
        i += 1
    for i in range(len(v)):
        l.append(define_winner(v[i]))
        i += 1
    if (l.count(1) == 1 and l.count(2) == 1) or (abs(x - o) > 1):
        return True
    else:
        return False


def analyze_field(h, v, d):
    if "_" in h[0] or "_" in h[1] or "_" in h[2]:
        return "Game not finished"
    elif impossible(h, v):
        return "Impossible"
    elif define_winner(h[0], h[1], h[2], v[0], v[1], v[2], d[0], d[1]) == 1:
        return "X wins"
    elif define_winner(h[0], h[1], h[2], v[0], v[1], v[2], d[0], d[1]) == 2:
        return "0 wins"
    else:
        return "Draw"


def play_game():
    while True:
        s = input("Insert string: ")
        h, v, d = divide(s)
        display(h)
        print(analyze_field(h, v, d))

play_game()

# s = 'XOXOOXXXO'
# h, v, d = divide(s)
# print(impossible(h, v))
