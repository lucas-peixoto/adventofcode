import re


def find_in_range(n, m):
    n = int(n)
    for line in m:
        line = line.split()
        line = [int(x) for x in line]
        if line[0] <= n <= (line[0] + line[2] - 1):
            return line[1] + (n - line[0])

    return n


def proccess_seed_from_location(location, maps):
    seed_map = {}
    next_value = location
    for k, m in maps.items():
        next_value = find_in_range(next_value, m)
        seed_map[k] = {"location": location, "value": next_value}

    return seed_map


def generate_seeds(seeds):
    seeds_ = []

    for i in range(0, len(seeds), 2):
        seeds_.append([int(seeds[i]), int(seeds[i + 1])])

    return seeds_


def is_in_seeds_ranges(seed, seeds_ranges):
    for seed_range in seeds_ranges:
        if seed_range[0] <= seed <= (seed_range[0] + seed_range[1]):
            return True

    return False


# with open('./fake-input.txt', 'r') as input_file:
with open('./05-input.txt', 'r') as input_file:
    input_data = input_file.read().split("\n\n")

    seeds_ = re.findall(r"\d+", input_data[0])
    seeds_ranges = generate_seeds(seeds_)

    seed_to_soil = input_data[1].splitlines()[1:]
    soil_to_fertilizer = input_data[2].splitlines()[1:]
    fertilizer_to_water = input_data[3].splitlines()[1:]
    water_to_light = input_data[4].splitlines()[1:]
    light_to_temperature = input_data[5].splitlines()[1:]
    temperature_to_humidity = input_data[6].splitlines()[1:]
    humidity_to_location = input_data[7].splitlines()[1:]

    maps = {
        "humidity_to_location": humidity_to_location,
        "temperature_to_humidity": temperature_to_humidity,
        "light_to_temperature": light_to_temperature,
        "water_to_light": water_to_light,
        "fertilizer_to_water": fertilizer_to_water,
        "soil_to_fertilizer": soil_to_fertilizer,
        "seed_to_soil": seed_to_soil,
    }

    i = -1
    lowest_seed = None
    while True:
        i += 1
        p_seed = proccess_seed_from_location(i, maps)

        if is_in_seeds_ranges(p_seed["seed_to_soil"]["value"], seeds_ranges):
            lowest_seed = p_seed["seed_to_soil"]["value"]
            break

    # print(lowest_seed)
    print(i)
    # 125742456
