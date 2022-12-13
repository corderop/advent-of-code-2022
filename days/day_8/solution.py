from utils import get_score_of_position, is_visible


def solution_1(input_text: str):
    lines = input_text.strip().splitlines()
    matrix = [[int(char) for char in line] for line in lines]
    reverse_matrix = [
        [matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))
    ]

    border_trees = len(matrix) * 2 + len(matrix[0]) * 2 - 4
    visible_trees = border_trees

    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            if is_visible(matrix, reverse_matrix, i, j):
                visible_trees += 1

    return visible_trees


def solution_2(input_text: str):
    lines = input_text.strip().splitlines()
    matrix = [[int(char) for char in line] for line in lines]
    reverse_matrix = [
        [matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))
    ]

    scores = []
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            score = get_score_of_position(matrix, reverse_matrix, i, j)
            scores.append(score)

    return max(scores)
