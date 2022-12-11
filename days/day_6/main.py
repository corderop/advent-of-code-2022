import os
from solution import solution_1, solution_2

dir_path = os.path.dirname(os.path.realpath(__file__))


if __name__ == "__main__":
    with open(f"{dir_path}/input.txt") as file:
        input_text = file.read()

    solution = solution_1(input_text)
    print("Solution 1:", solution)

    solution = solution_2(input_text)
    print("Solution 2:", solution)
