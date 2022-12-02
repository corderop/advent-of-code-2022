from solution_types import (
    Play,
    Points,
    PLAY_POINTS,
    WINNER_AGAINST,
    LOSER_AGAINST,
    Results,
)


def is_winner_against(play_1, play_2):
    return WINNER_AGAINST[play_1] == play_2


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


def get_match_points_by_oponent_and_result(play_1: Play, result: Results) -> int:
    if result == Results.WIN.value:
        return get_match_points(play_1, LOSER_AGAINST[play_1])

    if result == Results.DRAW.value:
        return get_match_points(play_1, play_1)

    if result == Results.LOST.value:
        return get_match_points(play_1, WINNER_AGAINST[play_1])
