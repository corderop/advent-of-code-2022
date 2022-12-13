from solution import solution_1, solution_2


class TestSolution1:
    def test_example(self):
        text = "30373\n25512\n65332\n33549\n35390\n"

        expected = 21
        result = solution_1(text)

        assert result == expected


class TestSolution2:
    pass
