input_data = open('./11-input.txt', 'r').readlines()
# input_data = open('./fake-input.txt', 'r').readlines()

columns = []
for i in range(len(input_data[0]) - 1):
    column = ''
    for j in range(len(input_data)):
        column += input_data[j][i]

    columns.append(column)
    if '#' not in column:
        columns.append(column)

new_input_data = []
rows = []
for i in range(len(input_data)):
    row = ''
    for j in range(len(columns)):
        row += columns[j][i]

    rows.append(row)
    if '#' not in row:
        rows.append(row)

input_data = rows
# print(''.join(new_input_data))

stars = []
for y in range(len(input_data)):
    for x in range(0, len(input_data[y])):
        if input_data[y][x] == '#':
            stars.append((x, y))

# print(stars)

stars_ = stars
pairs = []
while len(stars_) > 0:
    star = stars_.pop()
    for other_star in stars_:
        pairs.append((star, other_star))

# print(len(pairs), pairs)

length_sum = 0
for pair in pairs:
    length_sum += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

print(length_sum)
