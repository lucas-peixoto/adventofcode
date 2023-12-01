def first_num(text):
    for char in text:
        if char.isdigit():
            return char


def last_num(text: str):
    reversed_text = text[::-1]
    for char in reversed_text:
        if char.isdigit():
            return char


calibration_value = 0

with open("./01-input.txt") as input_file:
    input_data = input_file.read().splitlines()
    for line in input_data:
        fn = first_num(line)
        ln = last_num(line)
        line_value = fn+""+ln
        # print(line_value)
        calibration_value += int(line_value)

print(calibration_value)
# 54953
