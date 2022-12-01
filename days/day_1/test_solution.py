from .solution import solution_1


class TestSolution1:
    def test_simple_case():
        text = """1000\n\n1000\n2000\n"""

        expected = 3000
        result = solution_1(text)

        assert result == expected

    def test_another_case():
        text = """8000\n\n5000\n\n2000\n6000\n\n1000\n1000\n"""

        expected = 8000
        result = solution_1(text)

        assert result == expected

    def test_with_multiple_break_lines_after():
        text = """1000\n\n1000\n2000\n\n\n\n\n\n"""

        expected = 3000
        result = solution_1(text)

        assert result == expected

    def test_with_multiple_break_lines_before():
        text = """1000\n\n1000\n2000\n\n\n\n\n\n"""

        expected = 3000
        result = solution_1(text)

        assert result == expected
