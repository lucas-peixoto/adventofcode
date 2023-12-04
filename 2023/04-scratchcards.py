import re


def get_card_points(card):
    numbers = card.split(":")[1].split("|")
    winning_numbers = numbers[0]
    elf_numbers = numbers[1]

    winning_numbers = re.findall(r"(\d+)", winning_numbers)
    elf_numbers = re.findall(r"(\d+)", elf_numbers)

    points = 0
    for en in elf_numbers:
        if en in winning_numbers:
            points = points * 2 if points > 0 else 1

    return points


with open('./04-input.txt', 'r') as input_file:
    input_data = input_file.read().splitlines()
    points = 0
    for card in input_data:
        points += get_card_points(card)

    print(points)
    # 18519
