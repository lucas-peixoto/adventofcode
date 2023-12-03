import re


def find_gears(text, line_num):
    gears = []
    for match in re.finditer(r"\*", text):
        gears.append((match.group(), line_num, match.start(), match.end()))

    return gears


def find_numbers(text, line_num):
    numbers = []
    for match in re.finditer(r"(\d+)", text):
        numbers.append((match.group(), line_num, match.start(), match.end()))

    return numbers


def is_gear(char):
    return char == "*"


def update_gear(key_s, key_e, value, gears: dict):
    key = str(key_s) + ":" + str(key_e)
    if key in gears:
        gears[key].append(value)
    else:
        gears[key] = [value]


def update_gears_count(number_coord, gears, input_data):
    number = number_coord[0]
    line_num = number_coord[1]
    start = number_coord[2]
    end = number_coord[3]

    if start > 0:
        if is_gear(input_data[line_num][start - 1]):
            update_gear(line_num, (start - 1), number, gears)
    if end < len(input_data[line_num]):
        if is_gear(input_data[line_num][end]):
            update_gear(line_num, end, number, gears)

    if line_num > 0:
        if start > 0:
            if is_gear(input_data[line_num - 1][start - 1]):
                update_gear(line_num - 1, (start - 1), number, gears)
        if end < len(input_data[line_num - 1]):
            if is_gear(input_data[line_num - 1][end]):
                update_gear(line_num - 1, end, number, gears)
        for i in range(start, end):
            if is_gear(input_data[line_num - 1][i]):
                update_gear(line_num - 1, i, number, gears)

    if line_num < len(input_data) - 1:
        if start > 0:
            if is_gear(input_data[line_num + 1][start - 1]):
                update_gear(line_num + 1, start - 1, number, gears)
        if end < len(input_data[line_num + 1]):
            if is_gear(input_data[line_num + 1][end]):
                update_gear(line_num + 1, end, number, gears)
        for i in range(start, end):
            if is_gear(input_data[line_num + 1][i]):
                update_gear(line_num + 1, i, number, gears)


with open('./03-input.txt', 'r') as input_file:
    input_data = input_file.read().splitlines()
    numbers = []
    gears = {}
    gears_sum = 0

    for i, line in enumerate(input_data):
        numbers += find_numbers(line, i)

    for number in numbers:
        update_gears_count(number, gears, input_data)

    for _, gear in gears.items():
        if len(gear) == 2:
            gears_sum += int(gear[0]) * int(gear[1])

    print(gears_sum)
    # 81997870
