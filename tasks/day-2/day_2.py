import re
from inputs.input_getter import get_input, BASE_URL

"""12 red cubes, 13 green cubes, and 14 blue cubes"""
# PART 1 - 2545
cube_batch = {"red": 12, "green": 13, "blue": 14}


def is_set_impossible(red, green, blue):
    if any(
            [
                int(red[0]) > cube_batch.get("red") if red else 0,
                int(green[0]) > cube_batch.get("green") if green else 0,
                int(blue[0]) > cube_batch.get("blue") if blue else 0,
            ]
    ):
        return True


def get_sets(response_line):
    line_sets = response_line.split(": ")[1].split("; ")
    return line_sets


def get_all_colors_in_set(value_set):
    red = re.findall(r'(\d+)\sred', value_set)
    green = re.findall(r'(\d+)\sgreen', value_set)
    blue = re.findall(r'(\d+)\sblue', value_set)
    return red, green, blue


response = get_input(BASE_URL.format("2")).split("\n")
games_list = []
for line in response:
    if not line:
        continue
    game_dict = dict()
    game_dict["is_possible"] = True
    game_dict["name"] = int(line.split("Game ")[1].split(":")[0])
    sets = get_sets(line)

    for value_set in sets:
        red, green, blue = get_all_colors_in_set(value_set)
        if is_set_impossible(red, green, blue):
            game_dict["is_possible"] = False
            break
    games_list.append(game_dict)

result_1 = 0
for i in games_list:
    if i.get("is_possible"):
        result_1 += i.get("name")

print(f"PART-1 Result: {result_1}")

# Part 2 - 78111

result_2 = 0

for line in response:
    if not line:
        continue

    sets = get_sets(line)
    red_values = []
    green_values = []
    blue_values = []
    for value_set in sets:
        red, green, blue = get_all_colors_in_set(value_set)
        red_values.append(int(red[0])) if red else red_values.append(0)
        green_values.append(int(green[0])) if green else green_values.append(0)
        blue_values.append(int(blue[0])) if blue else blue_values.append(0)
    if all([red_values, green_values, blue_values]):
        result_2 += max(red_values) * max(green_values) * max(blue_values)


print(f"PART-2 Result: {result_2}")
