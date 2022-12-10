from solution import solution_1, solution_2


class TestSolution1:
    def test_example(self):
        text = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"

        expected = 2
        result = solution_1(text)

        assert result == expected


class TestSolution2:
    def test_example(self):
        text = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"

        expected = 4
        result = solution_2(text)

        assert result == expected
