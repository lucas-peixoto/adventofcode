def get_coord(start, coord):
    x = start[0] + coord[0]
    y = start[1] + coord[1]
    # print(x, y)
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

start = ()
for col, line in enumerate(input_data):
    row = line.find('S')
    if row != -1:
        start = {'x': row, 'y': col, 'value': 'S'}
        break

loop = []
pipe = {}
direction = ''
start_nsew = []
for d in 'NSEW':
    next_pipe = get_coord((start['x'], start['y']), rose[d])
    if next_pipe['value'] in possible_moves[d]:
        pipe = next_pipe
        direction = possible_moves[d][pipe['value']]
        pipe['direction'] = direction
        loop.append(start)
        start_nsew.append(d)
        loop.append(pipe)
        break

steps = 1
while True:
    steps += 1
    pipe = get_coord((pipe['x'], pipe['y']), rose[direction])
    if pipe['value'] == 'S':
        loop[0]['direction'] = direction
        start_nsew.append(direction)
        break

    pipe['direction'] = direction
    loop.append(pipe)
    direction = possible_moves[direction][pipe['value']]

start_eq = ''
if start_nsew[0] == 'S' and start_nsew[1] == 'W':
    start_eq = 'F'
elif start_nsew[0] == 'S' and start_nsew[1] == 'E':
    start_eq = '7'
elif start_nsew[0] == 'N' and start_nsew[1] == 'W':
    start_eq = 'J'
elif start_nsew[0] == 'N' and start_nsew[1] == 'E':
    start_eq = 'L'

loop_coords = set([(pipe['x'], pipe['y']) for pipe in loop])
# print(loop_coords)
direction = 'S'
pipe_start = None
for y in range(len(input_data)):
    for x in range(len(input_data[y])):
        if (x, y) in loop_coords:
            pipe_start = {'x': x, 'y': y, 'value': input_data[y][x], 'direction': direction}
            break
    if pipe_start:
        break

pipe = pipe_start
orientation = 'E'
internals = set()
print(pipe)
while True:
    pipe = get_coord((pipe['x'], pipe['y']), rose[pipe['direction']])

    if pipe['value'] == 'S':
        pipe['value'] = start_eq

    if (pipe['x'] == pipe_start['x']) and (pipe['y'] == pipe_start['y']):
        break

    print(f'orientation: {orientation}, direction: {direction}, value: {pipe["value"]}')
    if orientation == 'E':
        if direction == 'E' and pipe['value'] == 'J':
            orientation = 'W'
    if orientation == 'W':
        if direction == 'W' and pipe['value'] == 'F':
            orientation = 'E'
    if orientation == 'W':
        if direction == 'E' and pipe['value'] == '7':
            orientation = 'E'

    # if direction in 'NS':
    # print('pipe: ' + str(pipe))
    check = pipe
    while True:
        check = get_coord((check['x'], check['y']), rose[orientation])
        # print('check:' + str(check))
        # print()
        if (check['x'], check['y']) in loop_coords:
            break
        else:
            print('adding: ' + str(check))
            internals.add(str(check))

    print(pipe)
    print(orientation, direction)
    direction = possible_moves[direction][pipe['value']]
    pipe['direction'] = direction

print(internals)
print(len(internals))
# 6690
