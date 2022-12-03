def split_in_half(line: str) -> tuple[str, str]:
    half = len(line) // 2
    return (line[half:], line[:half])


def get_duplicated_item(compartment_1, compartment_2):
    compartment_1 = sorted(compartment_1)
    compartment_2 = sorted(compartment_2)

    for item in compartment_1:
        if item in compartment_2:
            return item


def get_common_item(group):
    backpack_1, backpack_2, backpack_3 = group
    backpack_1 = sorted(backpack_1)
    backpack_2 = sorted(backpack_2)
    backpack_3 = sorted(backpack_3)

    for item in backpack_1:
        if item in backpack_2 and item in backpack_3:
            return item


def split_backpacks_in_groups(backpacks):
    return [backpacks[i : i + 3] for i in range(0, len(backpacks), 3)]
