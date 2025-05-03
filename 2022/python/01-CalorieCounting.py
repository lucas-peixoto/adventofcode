with open('01-CalorieCounting.txt', 'r') as file:
    curr_elf = 0
    fat_elf = 0

    for line in file:
        fat_elf = curr_elf if curr_elf > fat_elf else fat_elf

        if line != '\n':
            curr_elf += int(line)
        else:
            curr_elf = 0

    print(fat_elf)

with open('01-CalorieCounting.txt', 'r') as file:
    elves = []
    curr_elf = 0

    for line in file:
        if line != '\n':
            curr_elf += int(line)
        else:
            elves.append(curr_elf)
            curr_elf = 0

    elves.sort(reverse=True)
    print(elves[0] + elves[1] + elves[2])
