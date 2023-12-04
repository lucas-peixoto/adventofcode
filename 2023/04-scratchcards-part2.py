import re


def get_card_matches(card):
    numbers = card.split(":")[1].split("|")
    winning_numbers = numbers[0]
    elf_numbers = numbers[1]

    winning_numbers = re.findall(r"(\d+)", winning_numbers)
    elf_numbers = re.findall(r"(\d+)", elf_numbers)

    points = 0
    for en in elf_numbers:
        if en in winning_numbers:
            points += 1

    return points


with open('./04-input.txt', 'r') as input_file:
    input_data = input_file.read().splitlines()
    cards = {}
    cards_count = {}

    for i, card in enumerate(input_data):
        points = get_card_matches(card)
        cards[i+1] = {"points": points, "count": 1}

    for i, card in cards.items():
        for j in range(i + 1, i + 1 + card["points"]):
            cards[j]["count"] += 1 * card["count"]

    print(sum([card["count"] for card in cards.values()]))
    # 11787590
