from utils import (
    add_elements_to_stack,
    get_elements_to_move,
    parse_layout,
    parse_moves,
    remove_elements_from_stack,
)


def solution(input_text: str, crate_mover_model: str):
    first_block, second_block = input_text.split("\n\n")
    layout = parse_layout(first_block)
    moves = parse_moves(second_block)

    for move in moves:
        number, original_stack, to_stack = move

        is_reverse = crate_mover_model == "9000"
        elements = get_elements_to_move(
            layout, number, original_stack, reverse=is_reverse
        )

        layout = remove_elements_from_stack(layout, number, original_stack)
        layout = add_elements_to_stack(layout, to_stack, elements)

    return "".join([stack.pop() for stack in layout if len(stack) > 0])


def solution_1(input_text: str):
    return solution(input_text, "9000")


def solution_2(input_text: str):
    return solution(input_text, "9001")
