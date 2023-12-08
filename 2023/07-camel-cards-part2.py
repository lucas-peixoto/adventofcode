input_data = open('./07-input.txt', 'r').read().splitlines()
# input_data = open('./fake-input.txt', 'r').read().splitlines()

points = {
    'A': 'a',
    'K': 'b',
    'Q': 'c',
    'T': 'e',
    '9': 'f',
    '8': 'g',
    '7': 'h',
    '6': 'i',
    '5': 'j',
    '4': 'k',
    '3': 'l',
    '2': 'm',
    'J': 'n',
}

cards_rank = []

for play in input_data:
    play = play.split()
    hand = play[0]
    bet = int(play[1])
    hand_set = set(hand)  # list(dict.fromkeys(hand))
    j_count = hand.count('J')

    if 'J' in hand_set:
        hand_set.remove('J')

    hand_count = [{"card": card, "count": hand.count(card)} for card in hand_set]
    hand_count.sort(key=lambda x: x["count"], reverse=True)
    # print(hand_set, hand_count)

    if len(hand_count) == 1 or len(hand_count) == 0:
        cards_rank.append((hand, bet, 7))
    elif len(hand_count) == 2:
        if hand_count[0]["count"] == 4 - j_count:
            cards_rank.append((hand, bet, 6))
        else:
            cards_rank.append((hand, bet, 5))
    elif len(hand_count) == 3:
        if hand_count[0]["count"] == 3 - j_count:
            cards_rank.append((hand, bet, 4))
        else:
            cards_rank.append((hand, bet, 3))
    elif len(hand_count) == 4:
        cards_rank.append((hand, bet, 2))
    else:
        cards_rank.append((hand, bet, 1))

cards_rank.sort(key=lambda x: (-x[2], ''.join([str(points[card]) for card in x[0]])))
cards_rank.reverse()
# print(cards_rank)

result = sum([(i+1) * cr[1] for i, cr in enumerate(cards_rank)])
print(result)
# 249400220
