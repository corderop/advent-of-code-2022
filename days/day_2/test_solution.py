from .solution import solution_1, solution_2


class TestSolution1:
    def test_example_case(self):
        text = "A Y\nB X\nC Z"

        expected = 15
        result = solution_1(text)

        assert result == expected


class TestSolution2:
    pass
