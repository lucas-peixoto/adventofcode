import re

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
numbers_regex = re.compile(r"|".join(numbers.keys()))
reversed_numbers_regex = re.compile(r"|".join([key[::-1] for key in numbers.keys()]))


def first_num(text):
    for i, char in enumerate(text):
        if char.isdigit():
            return i, char


def first_spelled_num(text):
    match = re.search(numbers_regex, text)
    if match:
        start = match.start()
        # print(str(start) + ": " + text[start])
        # print(match.group())
        return start, numbers[match.group()]
    else:
        return 1_000_000_000, -1


def last_spelled_num(text):
    match = re.search(reversed_numbers_regex, text)
    if match:
        start = match.start()
        # print(str(start) + ": " + text[start])
        # print(match.group())
        return start, numbers[match.group()[::-1]]
    else:
        return 1_000_000_000, -1


calibration_value = 0

with open("./01-input.txt") as input_file:
    input_data = input_file.read().splitlines()
    for line in input_data:
        fn_ = first_num(line)
        ln_ = first_num(line[::-1])
        fsn = first_spelled_num(line)
        lsn = last_spelled_num(line[::-1])

        fn = fn_[1] if fn_[0] <= fsn[0] else fsn[1]
        ln = ln_[1] if ln_[0] <= lsn[0] else lsn[1]

        line_value = str(fn) + "" + str(ln)
        # print(line_value)
        calibration_value += int(line_value)

print(calibration_value)
# 53868
