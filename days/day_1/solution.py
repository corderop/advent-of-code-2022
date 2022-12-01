from utils import get_number_of_calories_for_every_elf, get_top_3_elves


def solution_1(input_text: str) -> int:
    elves_calories = get_number_of_calories_for_every_elf(input_text)
    return max(elves_calories)


def solution_2(input_text: str) -> int:
    elves_calories = get_number_of_calories_for_every_elf(input_text)
    top_3_elves = get_top_3_elves(elves_calories)
    return sum(top_3_elves)
