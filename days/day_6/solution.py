from utils import has_duplicated_values


def solution(input_text: str, message_size: int):
    for i in range(0, len(input_text)):
        four_char_section = input_text[i : i + message_size]
        if not has_duplicated_values(four_char_section):
            return i + message_size


def solution_1(input_text: str):
    return solution(input_text, message_size=4)


def solution_2(input_text: str):
    return solution(input_text, message_size=14)
