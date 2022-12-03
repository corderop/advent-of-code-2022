def split_in_half(line: str) -> tuple[str, str]:
    half = len(line) // 2
    return (line[half:], line[:half])


def get_duplicated_item(compartment_1, compartment_2):
    compartment_1 = sorted(compartment_1)
    compartment_2 = sorted(compartment_2)

    for item in compartment_1:
        if item in compartment_2:
            return item
