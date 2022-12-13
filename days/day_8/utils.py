def is_visible(matrix, reverse_matrix, i, j):
    height = matrix[i][j]
    max_left = max(matrix[i][:j])
    max_right = max(matrix[i][j + 1 : len(matrix)])
    max_top = max(reverse_matrix[j][:i])
    max_bottom = max(reverse_matrix[j][i + 1 : len(reverse_matrix)])

    return (
        height > max_left
        or height > max_top
        or height > max_right
        or height > max_bottom
    )


def get_score_of_position(matrix, reverse_matrix, i, j):
    value = matrix[i][j]

    top_row = list(reversed(reverse_matrix[j][:i]))
    top = get_trees_seen_at(top_row, value)

    left_row = list(reversed(matrix[i][:j]))
    left = get_trees_seen_at(left_row, value)

    right_row = matrix[i][j + 1 : len(matrix)]
    right = get_trees_seen_at(right_row, value)

    bottom_row = reverse_matrix[j][i + 1 : len(reverse_matrix)]
    bottom = get_trees_seen_at(bottom_row, value)

    return top * left * right * bottom


def get_trees_seen_at(row, value):
    number_of_trees = 0

    for tree in row:
        number_of_trees += 1
        if tree >= value:
            return number_of_trees

    return number_of_trees
