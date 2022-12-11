from solution import solution_1, solution_2


class TestSolution1:
    def test_example_1(self):
        text = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

        expected = 7
        result = solution_1(text)

        assert result == expected

    def test_example_2(self):
        text = "bvwbjplbgvbhsrlpgdmjqwftvncz"

        expected = 5
        result = solution_1(text)

        assert result == expected

    def test_example_3(self):
        text = "nppdvjthqldpwncqszvftbrmjlhg"

        expected = 6
        result = solution_1(text)

        assert result == expected

    def test_example_4(self):
        text = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

        expected = 10
        result = solution_1(text)

        assert result == expected

    def test_example_5(self):
        text = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

        expected = 11
        result = solution_1(text)

        assert result == expected


class TestSolution2:
    def test_example_1(self):
        text = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

        expected = 19
        result = solution_2(text)

        assert result == expected

    def test_example_2(self):
        text = "bvwbjplbgvbhsrlpgdmjqwftvncz"

        expected = 23
        result = solution_2(text)

        assert result == expected

    def test_example_3(self):
        text = "nppdvjthqldpwncqszvftbrmjlhg"

        expected = 23
        result = solution_2(text)

        assert result == expected

    def test_example_4(self):
        text = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

        expected = 29
        result = solution_2(text)

        assert result == expected

    def test_example_5(self):
        text = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

        expected = 26
        result = solution_2(text)

        assert result == expected
