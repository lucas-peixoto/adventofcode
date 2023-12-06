import re


def find_in_range(seed, m):
    seed = int(seed)
    for line in m:
        line = line.split()
        line = [int(x) for x in line]
        if line[1] <= seed <= (line[1] + line[2]):
            return line[0] + (seed - line[1])

    return seed


def proccess_seed(seed, maps):
    seed_map = {}
    next_value = seed
    for k, m in maps.items():
        next_value = find_in_range(next_value, m)
        seed_map[k] = {"seed": seed, "value": next_value}

    return seed_map


with open('./05-input.txt', 'r') as input_file:
    input_data = input_file.read().split("\n\n")

    seeds = re.findall(r"\d+", input_data[0])

    seed_to_soil = input_data[1].splitlines()[1:]
    soil_to_fertilizer = input_data[2].splitlines()[1:]
    fertilizer_to_water = input_data[3].splitlines()[1:]
    water_to_light = input_data[4].splitlines()[1:]
    light_to_temperature = input_data[5].splitlines()[1:]
    temperature_to_humidity = input_data[6].splitlines()[1:]
    humidity_to_location = input_data[7].splitlines()[1:]

    maps = {
        "seed_to_soil": seed_to_soil,
        "soil_to_fertilizer": soil_to_fertilizer,
        "fertilizer_to_water": fertilizer_to_water,
        "water_to_light": water_to_light,
        "light_to_temperature": light_to_temperature,
        "temperature_to_humidity": temperature_to_humidity,
        "humidity_to_location": humidity_to_location
    }

    seeds_maps = {}
    
    for seed in seeds:
        seeds_maps[seed] = proccess_seed(seed, maps)

    lowest_location = None
    for seed, seed_map in seeds_maps.items():
        # print(seed, seed_map["humidity_to_location"]["value"])
        if lowest_location is None or seed_map["humidity_to_location"]["value"] < lowest_location["lowest_location"]:
            lowest_location = {"seed": seed, "lowest_location": seed_map["humidity_to_location"]["value"]}

    # print(lowest_location)
    print(lowest_location["lowest_location"])
    # 196167384
