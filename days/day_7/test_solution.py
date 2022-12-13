from solution import solution_1, solution_2


class TestSolution1:
    def test_example(self):
        text = (
            "$ cd /\n"
            "$ ls\n"
            "dir a\n"
            "14848514 b.txt\n"
            "8504156 c.dat\n"
            "dir d\n"
            "$ cd a\n"
            "$ ls\n"
            "dir e\n"
            "29116 f\n"
            "2557 g\n"
            "62596 h.lst\n"
            "$ cd e\n"
            "$ ls\n"
            "584 i\n"
            "$ cd ..\n"
            "$ cd ..\n"
            "$ cd d\n"
            "$ ls\n"
            "4060174 j\n"
            "8033020 d.log\n"
            "5626152 d.ext\n"
            "7214296 k"
        )

        expected = 95437
        result = solution_1(text)

        assert result == expected


class TestSolution2:
    def test_example(self):
        text = (
            "$ cd /\n"
            "$ ls\n"
            "dir a\n"
            "14848514 b.txt\n"
            "8504156 c.dat\n"
            "dir d\n"
            "$ cd a\n"
            "$ ls\n"
            "dir e\n"
            "29116 f\n"
            "2557 g\n"
            "62596 h.lst\n"
            "$ cd e\n"
            "$ ls\n"
            "584 i\n"
            "$ cd ..\n"
            "$ cd ..\n"
            "$ cd d\n"
            "$ ls\n"
            "4060174 j\n"
            "8033020 d.log\n"
            "5626152 d.ext\n"
            "7214296 k"
        )

        expected = 24933642
        result = solution_2(text)

        assert result == expected
