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
