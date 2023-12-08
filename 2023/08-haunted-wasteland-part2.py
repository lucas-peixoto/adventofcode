import math

input_data = open('./08-input.txt', 'r').read().splitlines()
# input_data = open('./fake-input.txt', 'r').read().splitlines()

rl_map = {'L': 0, 'R': 1}
rl = input_data.pop(0)
input_data.pop(0)

moves = {line.split('=')[0].strip(): (line.split('=')[0].strip(), line.split('=')[1].strip().strip('()').split(', '))
         for line in input_data}
# print(rl, moves)

steps = 0
curr_rl_i = 0
curr_move_keys = list(filter(lambda x: x.endswith('A'), moves.keys()))
z_found = []
while True:
    steps += 1
    curr_move_keys = [moves[curr_move_key][1][rl_map[rl[curr_rl_i]]] for curr_move_key in curr_move_keys]

    for move in curr_move_keys:
        if move.endswith('Z'):
            z_found.append(steps)
            curr_move_keys.remove(move)

    if len(curr_move_keys) == 0:
        break

    curr_rl_i = curr_rl_i + 1 if (len(rl) - 1) > curr_rl_i else 0

# print(z_found)
print(math.lcm(*z_found))
# 13_289_612_809_129
