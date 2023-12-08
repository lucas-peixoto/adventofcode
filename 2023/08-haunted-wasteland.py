input_data = open('./08-input.txt', 'r').read().splitlines()
# input_data = open('./fake-input.txt', 'r').read().splitlines()

rl_map = {'L': 0, 'R': 1}
rl = input_data.pop(0)
input_data.pop(0)

moves = {line.split('=')[0].strip(): (line.split('=')[0].strip(), line.split('=')[1].strip().strip('()').split(', ')) for line in input_data}
# print(rl, moves)

steps = 0
curr_rl_i = 0
curr_move_key = 'AAA'
while curr_move_key != 'ZZZ':
    steps += 1
    curr_move = moves[curr_move_key]
    curr_move_key = curr_move[1][rl_map[rl[curr_rl_i]]]
    curr_rl_i = curr_rl_i + 1 if (len(rl) - 1) > curr_rl_i else 0
    # print(curr_move, curr_move_key)

print(steps)
# 20777
