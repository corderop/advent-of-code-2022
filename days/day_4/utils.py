def parse_pairs_from_text(input_text):
    lines = input_text.splitlines()
    pairs = [line.split(",") for line in lines]
    pairs = [[tuple(map(int, elf.split("-"))) for elf in pair] for pair in pairs]
    return pairs


def does_fully_contain(elf_1, elf_2):
    return elf_1[0] <= elf_2[0] and elf_1[1] >= elf_2[1]


def does_overlap(elf_1, elf_2):
    return elf_1[1] >= elf_2[0] and elf_1[1] <= elf_2[1]
