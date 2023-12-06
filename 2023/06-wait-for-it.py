import re
from functools import reduce

input_data = open('./06-input.txt', 'r').read().splitlines()

times = list(map(int, re.findall(r"\d+", input_data[0].split(":")[1])))
distances = list(map(int, re.findall(r"\d+", input_data[1].split(":")[1])))

results = {}
for t, d in zip(times, distances):
    results[t] = []
    for hold_time in range(t):
        distance = hold_time * (t - hold_time)
        if distance > d:
            results[t].append({"hold_time": hold_time, "distance": distance})

possibilities = []
for time, distances in results.items():
    possibilities.append(len(distances))

print(reduce((lambda x, y: x * y), possibilities))
# 741000
