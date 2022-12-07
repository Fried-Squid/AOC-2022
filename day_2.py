def solve_p1(data):
    data = [x.split(" ") for x in data]

    player_moves_points = sum([(1, 2, 3)[ord(x[1]) - 88] for x in data])  # works

    data = list(filter(lambda a: ord(a[0]) - 65 != ord(a[1]) - 88, data))
    draws = (2500 - len(data))  # works?

    temp = len(data)
    challenge_2_input = list(filter(
        lambda a: (((a[0] == "A") * (a[1] == "Z")) + ((a[0] == "B") * (a[1] == "X")) + ((a[0] == "C") * (a[1] == "Y"))),
        data))
    wins = (temp - len(challenge_2_input))

    print(int(wins * 6 + draws * 3 + player_moves_points))


def solve_p2(data):
    data = [x.split(" ") for x in data]

    tot = 0
    for each in data:
        if each[1] == "Y":
            tot += (1, 2, 3)[ord(each[0]) - 65] + 3
        if each[1] == "X":  # loose
            tot += (3, 1, 2)[ord(each[0]) - 65]
        if each[1] == "Z":  # win
            tot += (2, 3, 1)[ord(each[0]) - 65] + 6
    print(tot)
