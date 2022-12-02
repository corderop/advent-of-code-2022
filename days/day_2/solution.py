from enum import Enum


class Play(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class Points(Enum):
    WIN = 6
    DRAW = 3
    LOST = 0


PLAY_POINTS = {
    Play.ROCK.value: 1,
    Play.PAPER.value: 2,
    Play.SCISSORS.value: 3,
}


def is_winner_against(play_1, play_2):
    winner_against = {
        Play.ROCK.value: Play.SCISSORS.value,
        Play.PAPER.value: Play.ROCK.value,
        Play.SCISSORS.value: Play.PAPER.value,
    }
    return winner_against[play_1] == play_2


def get_matches(input_text: str) -> list[tuple[str, str]]:
    matches = input_text.strip().split("\n")
    return [tuple(match.split(" ")) for match in matches]


def get_match_points(play_1: Play, play_2: Play) -> int:
    points = PLAY_POINTS[play_2]

    if play_1 == play_2:
        return points + Points.DRAW.value

    if is_winner_against(play_2, play_1):
        return points + Points.WIN.value

    return points


def get_points_for_solution(solution: dict, matches: list[tuple[str, str]]) -> int:
    points = 0

    for match in matches:
        play_1, play_2 = match[0], solution[match[1]]
        match_points = get_match_points(play_1, play_2)
        points += match_points

    return points


def solution_1(input_text: str) -> int:
    matches = get_matches(input_text)
    solution = {
        "X": Play.ROCK.value,
        "Y": Play.PAPER.value,
        "Z": Play.SCISSORS.value,
    }
    return get_points_for_solution(solution, matches)


def solution_2(input_text: str) -> int:
    pass
