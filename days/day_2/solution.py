from solution_types import (
    Play,
    RESULT_BY_CODE,
)
from utils import (
    get_match_points_by_oponent_and_result,
    get_matches,
    get_points_for_solution,
)


def solution_1(input_text: str) -> int:
    matches = get_matches(input_text)
    solution = {
        "X": Play.ROCK.value,
        "Y": Play.PAPER.value,
        "Z": Play.SCISSORS.value,
    }
    return get_points_for_solution(solution, matches)


def solution_2(input_text: str) -> int:
    matches = get_matches(input_text)
    points = 0

    for match in matches:
        play_1, result = match[0], RESULT_BY_CODE[match[1]]
        points += get_match_points_by_oponent_and_result(play_1, result)

    return points
