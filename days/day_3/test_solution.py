from solution import solution_1, solution_2


class TestSolution1:
    def test_example(self):
        text = (
            "vJrwpWtwJgWrhcsFMMfFFhFp\n"
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n"
            "PmmdzqPrVvPwwTWBwg\n"
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n"
            "ttgJtRGJQctTZtZT\n"
            "CrZsJsPPZsGzwwsLwLmpwMDw\n"
        )

        expected = 157
        result = solution_1(text)

        assert result == expected


class TestSolution2:
    pass
