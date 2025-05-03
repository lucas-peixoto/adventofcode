with open('02-RockPaperScissors.txt', 'r') as file:
    A = X = 1
    B = Y = 2
    C = Z = 3

    results = {
        'A Z': 3,
        'B X': 1,
        'C Y': 2,
        'A X': 4,
        'B Y': 5,
        'C Z': 6,
        'A Y': 8,
        'B Z': 9,
        'C X': 7,
    }

    points = 0

    for line in file:
        points += results[line.rstrip()]

    print(points)
