import re
from functools import reduce

input_data = open('./06-input.txt', 'r').read().splitlines()
# input_data = open('./fake-input.txt', 'r').read().splitlines()

time = int(''.join(re.findall(r"\d+", input_data[0].split(":")[1])))
distance = int(''.join(re.findall(r"\d+", input_data[1].split(":")[1])))

first_win = 0
last_win = 0
hold_time = 0
while True:
    hold_time += 1
    d = hold_time * (time - hold_time)
    if d > distance:
        first_win = hold_time
        break

hold_time = time - 1

while True:
    hold_time -= 1
    d = hold_time * (time - hold_time)
    if d > distance:
        last_win = hold_time
        break


# print(first_win, last_win)
print(last_win - first_win + 1)
# 38220708
