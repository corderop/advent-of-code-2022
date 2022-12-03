from solution_types import POINTS
from utils import (
    get_common_item,
    get_duplicated_item,
    split_backpacks_in_groups,
    split_in_half,
)


def solution_1(input_text: str):
    points = 0
    lines = input_text.splitlines()
    backpacks = [split_in_half(line) for line in lines]

    for backpack in backpacks:
        compartment_1, compartment_2 = backpack
        duplicated_item = get_duplicated_item(compartment_1, compartment_2)
        points += POINTS.get(duplicated_item)

    return points


def solution_2(input_text: str):
    points = 0
    backpacks = input_text.splitlines()
    groups = split_backpacks_in_groups(backpacks)

    for group in groups:
        item = get_common_item(group)
        points += POINTS.get(item)

    return points
