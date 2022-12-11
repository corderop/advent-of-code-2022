import re


def add_elements_to_stack(layout, stack, elements):
    layout[stack - 1] = layout[stack - 1] + elements

    return layout


def remove_elements_from_stack(layout, number, stack):
    del layout[stack - 1][-number:]

    return layout


def get_elements_to_move(layout, number, stack, reverse=True):
    elements = layout[stack - 1][-number:]
    if reverse:
        elements.reverse()

    return elements


def parse_layout(layout: str):
    lines = layout.splitlines()[:-1]
    lines = [clean_line_information(line) for line in lines]

    bottom_line = lines.pop()
    stacks = [[letter] for letter in bottom_line]
    while len(lines) > 0:
        line = lines.pop()
        for index, letter in enumerate(line):
            if letter:
                stacks[index].append(letter)

    return stacks


def parse_moves(moves: str):
    lines = moves.splitlines()
    return [extract_groups_from_line(line) for line in lines]


def extract_groups_from_line(line):
    regex = r"move (\d+) from (\d+) to (\d+)"

    result = re.search(regex, line)
    groups = result.groups()

    return [int(groups[0]), int(groups[1]), int(groups[2])]


def clean_line_information(line: str):
    EMPTY_POSITION = "    "
    return (
        line.replace(EMPTY_POSITION, " 1")
        .replace(" ", "\t")
        .replace("[", "")
        .replace("]", "")
        .replace("1", "")
        .split("\t")
    )
