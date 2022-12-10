from utils import does_fully_contain, parse_pairs_from_text, does_overlap


def solution_1(input_text: str):
    pairs = parse_pairs_from_text(input_text)
    counter = 0

    for pair in pairs:
        elf_1, elf_2 = pair
        if does_fully_contain(elf_1, elf_2) or does_fully_contain(elf_2, elf_1):
            counter += 1

    return counter


def solution_2(input_text: str):
    pairs = parse_pairs_from_text(input_text)
    counter = 0

    for pair in pairs:
        elf_1, elf_2 = pair
        if does_overlap(elf_1, elf_2) or does_overlap(elf_2, elf_1):
            counter += 1

    return counter
