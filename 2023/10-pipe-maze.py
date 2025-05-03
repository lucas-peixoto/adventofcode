import math


def get_coord(start, coord):
    x = start[0] + coord[0]
    y = start[1] + coord[1]
    return {'x': x, 'y': y, 'value': input_data[y][x]}


input_data = open('./10-input.txt', 'r').readlines()
# input_data = open('./fake-input.txt', 'r').readlines()

rose = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0),
}

possible_moves = {
    'N': {'|': 'N', '7': 'W', 'F': 'E'},
    'S': {'|': 'S', 'L': 'E', 'J': 'W'},
    'E': {'-': 'E', 'J': 'N', '7': 'S'},
    'W': {'-': 'W', 'L': 'N', 'F': 'S'},
}

start = (0, 0)
for col, line in enumerate(input_data):
    row = line.find('S')
    if row != -1:
        start = (row, col)
        break

pipe = {}
direction = ''
for d in 'NSEW':
    next_pipe = get_coord(start, rose[d])
    if next_pipe['value'] in possible_moves[d]:
        pipe = next_pipe
        direction = possible_moves[d][pipe['value']]
        # print('pipe: ' + str(pipe))
        # print('direction: ' + direction)
        break

steps = 1
while True:
    steps += 1
    pipe = get_coord((pipe['x'], pipe['y']), rose[direction])
    if pipe['value'] == 'S':
        break

    direction = possible_moves[direction][pipe['value']]

    # print('pipe: ' + str(pipe))
    # print('direction: ' + direction)

print(math.ceil(steps / 2))
# 6690
