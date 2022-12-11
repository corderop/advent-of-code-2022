from solution import solution_1, solution_2
from utils import parse_layout, parse_moves


class TestSolution1:
    def test_example(self):
        text = (
            "    [D]    \n"
            "[N] [C]    \n"
            "[Z] [M] [P]\n"
            " 1   2   3 \n"
            "\n"
            "move 1 from 2 to 1\n"
            "move 3 from 1 to 3\n"
            "move 2 from 2 to 1\n"
            "move 1 from 1 to 2\n"
        )

        expected = "CMZ"
        result = solution_1(text)

        assert result == expected

    def test_parse_layout(self):
        text = "    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 "

        result = parse_layout(text)

        assert isinstance(result, list)
        assert len(result) == 3
        assert result[0] == ["Z", "N"]
        assert result[1] == ["M", "C", "D"]
        assert result[2] == ["P"]

    def test_parse_moves(self):
        text = (
            "move 1 from 2 to 1\n"
            "move 3 from 1 to 3\n"
            "move 2 from 2 to 1\n"
            "move 1 from 1 to 2\n"
        )

        result = parse_moves(text)

        assert isinstance(result, list)
        assert len(result) == 4
        assert result[0] == [1, 2, 1]
        assert result[1] == [3, 1, 3]
        assert result[2] == [2, 2, 1]
        assert result[3] == [1, 1, 2]

    def test_parse_layout_from_input(self):
        text = (
            "[N]     [Q]         [N]            \n"
            "[R]     [F] [Q]     [G] [M]        \n"
            "[J]     [Z] [T]     [R] [H] [J]    \n"
            "[T] [H] [G] [R]     [B] [N] [T]    \n"
            "[Z] [J] [J] [G] [F] [Z] [S] [M]    \n"
            "[B] [N] [N] [N] [Q] [W] [L] [Q] [S]\n"
            "[D] [S] [R] [V] [T] [C] [C] [N] [G]\n"
            "[F] [R] [C] [F] [L] [Q] [F] [D] [P]\n"
            " 1   2   3   4   5   6   7   8   9 "
        )

        result = parse_layout(text)

        assert len(result) == 9
        assert result[0] == ["F", "D", "B", "Z", "T", "J", "R", "N"]
        assert result[1] == ["R", "S", "N", "J", "H"]
        assert result[2] == ["C", "R", "N", "J", "G", "Z", "F", "Q"]
        assert result[3] == ["F", "V", "N", "G", "R", "T", "Q"]
        assert result[4] == ["L", "T", "Q", "F"]
        assert result[5] == ["Q", "C", "W", "Z", "B", "R", "G", "N"]
        assert result[6] == ["F", "C", "L", "S", "N", "H", "M"]
        assert result[7] == ["D", "N", "Q", "M", "T", "J"]
        assert result[8] == ["P", "G", "S"]


class TestSolution2:
    pass
