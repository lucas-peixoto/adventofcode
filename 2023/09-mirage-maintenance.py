input_data = open('./09-input.txt', 'r').readlines()
# input_data = open('./fake-input.txt', 'r').readlines()


def get_next(numbers) -> int:
    new_numbers = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
    return new_numbers[0] if len(set(new_numbers)) == 1 else new_numbers[-1] + get_next(new_numbers)


new_items = []
for line in input_data:
    numbers = list(map(int, line.split()))
    new_items.append(numbers[-1] + get_next(numbers))

print(sum(new_items))
# 1762065988
