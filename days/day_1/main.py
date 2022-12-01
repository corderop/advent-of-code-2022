from solution import solution_1


if __name__ == "__main__":
    with open("input.txt") as file:
        input_text = file.read()

    solution = solution_1(input_text)
    print("Solution 1:", solution)
