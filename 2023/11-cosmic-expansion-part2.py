import re

input_data = open('./11-input.txt', 'r').readlines()
# input_data = open('./fake-input.txt', 'r').readlines()

stars = []
for x in range(len(input_data)):
    if '#' in input_data[x]:
        stars.extend([(x, m.start()) for m in re.finditer('#', input_data[x])])

# print("stars:", len(stars))
# print(stars)

stars_ = stars.copy()
for i in range(len(input_data[0]) - 1):
    column_has_star = False
    for j in range(len(input_data)):
        if input_data[j][i] == '#':
            column_has_star = True
            break

    if not column_has_star:
        for idx, star in enumerate(stars):
            if star[0] > i:
                stars_[idx] = (stars_[idx][0] + 1000000 - 1, stars_[idx][1])

stars = stars_.copy()
# print("stars:", len(stars))
# print(stars)

for i, row in enumerate(input_data):
    if '#' not in row:
        for idx, star in enumerate(stars):
            if star[1] > i:
                stars_[idx] = (stars_[idx][0], stars_[idx][1] + 1000000 - 1)

stars = stars_.copy()
# print("stars:", len(stars))
# print(stars)

stars_ = stars.copy()
pairs = []
while len(stars_) > 0:
    star = stars_.pop()
    for other_star in stars_:
        pairs.append((star, other_star))

# print(len(pairs), pairs)

length_sum = 0
for pair in pairs:
    length_sum += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])

# print(len(pairs), pairs)
print(length_sum)
# 678626878094
# 678626878094
# 590669417290
# 590668826626
# 682272195830
