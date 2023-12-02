def verify_play(play: str, bag: dict):
    max_red = 0
    max_green = 0
    max_blue = 0

    play = play.split(',')
    for p in play:
        p = p.strip().split()
        if p[1] == 'red' and int(p[0]) > max_red:
            max_red = int(p[0])
        elif p[1] == 'green' and int(p[0]) > max_green:
            max_green = int(p[0])
        elif p[1] == 'blue' and int(p[0]) > max_blue:
            max_blue = int(p[0])

    return not (max_red > bag['red'] or max_green > bag['green'] or max_blue > bag['blue'])


def verify_game(game: str, bag: dict):
    game = game.split(':')
    game_num = game[0].split()[1]
    plays = game[1].split(';')

    for play in plays:
        if not verify_play(play, bag):
            return False
    return game_num


with open('./02-input.txt', 'r') as input_file:
    bag = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    game_sum = 0
    input_data = input_file.read().splitlines()
    for line in input_data:
        result = verify_game(line, bag)
        print(result)
        if result is not False:
            game_sum += int(result)

    print()
    print(game_sum)
