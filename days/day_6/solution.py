from utils import has_duplicated_values


def solution_1(input_text: str):
    for i in range(0, len(input_text)):
        four_char_section = input_text[i : i + 4]
        if not has_duplicated_values(four_char_section):
            return i + 4


def solution_2(input_text: str):
    pass
