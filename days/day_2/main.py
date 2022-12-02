from solution import solution_1, solution_2


if __name__ == "__main__":
    with open("input.txt") as file:
        input_text = file.read()

    solution = solution_1(input_text)
    print("Solution 1:", solution)

    solution = solution_2(input_text)
    print("Solution 2:", solution)
