def get_top_3_elves(elves_calories):
    elves_calories.sort(reverse=True)
    top_3_elves = elves_calories[:3]
    return top_3_elves


def get_number_of_calories_for_every_elf(input_text):
    elves_food = split_every_elf_food(input_text)
    elves_items = split_items_of_every_elf(elves_food)
    elves_calories = calculate_total_calories_of_every_elf(elves_items)
    return elves_calories


def calculate_total_calories_of_every_elf(elves_food):
    return [sum(convert_str_list_to_int(elf)) for elf in elves_food]


def split_items_of_every_elf(elves_food):
    return [elf.split("\n") for elf in elves_food]


def split_every_elf_food(input_text):
    return input_text.strip().split("\n\n")


def convert_str_list_to_int(str_list: list[str]) -> list[int]:
    return [int(str) for str in str_list]
