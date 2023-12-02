def get_play(play: str):
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

    return max_red, max_green, max_blue


def get_game_power(game: str):
    game = game.split(':')
    plays = game[1].split(';')
    game_max = [0, 0, 0]

    for play in plays:
        play_max = get_play(play)
        if game_max[0] < play_max[0]:
            game_max[0] = play_max[0]

        if game_max[1] < play_max[1]:
            game_max[1] = play_max[1]

        if game_max[2] < play_max[2]:
            game_max[2] = play_max[2]

    return game_max[0] * game_max[1] * game_max[2]


with open('./02-input.txt', 'r') as input_file:
    power_sum = 0
    input_data = input_file.read().splitlines()
    for line in input_data:
        result = get_game_power(line)
        # print(result)
        power_sum += result

    print()
    print(power_sum)
