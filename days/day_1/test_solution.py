from solution import solution_1, solution_2


class TestSolution1:
    def test_simple_case(self):
        text = """1000\n\n1000\n2000\n"""

        expected = 3000
        result = solution_1(text)

        assert result == expected

    def test_another_case(self):
        text = """8000\n\n5000\n\n2000\n6000\n\n1000\n1000\n"""

        expected = 8000
        result = solution_1(text)

        assert result == expected

    def test_with_multiple_break_lines_after(self):
        text = """1000\n\n1000\n2000\n\n\n\n\n\n"""

        expected = 3000
        result = solution_1(text)

        assert result == expected

    def test_with_multiple_break_lines_before(self):
        text = """1000\n\n1000\n2000\n\n\n\n\n\n"""

        expected = 3000
        result = solution_1(text)

        assert result == expected


class TestSolution2:
    def test_simple_case(self):
        text = """8000\n\n5000\n\n2000\n6000\n\n1000\n1000\n"""

        expected = 21000
        result = solution_2(text)

        assert result == expected
