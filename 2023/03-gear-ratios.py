import re


def find_numbers(text, line_num):
    numbers = []
    for match in re.finditer(r"(\d+)", text):
        numbers.append((match.group(), line_num, match.start(), match.end()))

    return numbers


def is_symbol(char):
    return not char.isdigit() and not char == "."


def has_adjacent_symbol(number_coord, input_data):
    line_num = number_coord[1]
    start = number_coord[2]
    end = number_coord[3]

    if start > 0:
        if is_symbol(input_data[line_num][start - 1]):
            return True
    if end < len(input_data[line_num]):
        if is_symbol(input_data[line_num][end]):
            return True

    if line_num > 0:
        if start > 0:
            if is_symbol(input_data[line_num - 1][start - 1]):
                return True
        if end < len(input_data[line_num - 1]):
            if is_symbol(input_data[line_num - 1][end]):
                return True
        for i in range(start, end):
            if is_symbol(input_data[line_num - 1][i]):
                return True

    if line_num < len(input_data) - 1:
        if start > 0:
            if is_symbol(input_data[line_num + 1][start - 1]):
                return True
        if end < len(input_data[line_num + 1]):
            if is_symbol(input_data[line_num + 1][end]):
                return True
        for i in range(start, end):
            if is_symbol(input_data[line_num + 1][i]):
                return True

    return False


with open('./03-input.txt', 'r') as input_file:
    input_data = input_file.read().splitlines()
    numbers = []
    numbers_sum = 0

    for i, line in enumerate(input_data):
        numbers += find_numbers(line, i)

    for number in numbers:
        if has_adjacent_symbol(number, input_data):
            # print(number)
            numbers_sum += int(number[0])

    print(numbers_sum)
    # 550934
