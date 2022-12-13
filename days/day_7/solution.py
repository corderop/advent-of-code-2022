from utils import (
    calculate_size_of_all_folders,
    get_navigation_destination,
    is_directory,
    is_ls,
    is_navigation,
)
from file_tree import FileTree


def solution_1(input_text: str):
    lines = input_text.splitlines()
    file_tree = FileTree()

    for line in lines:
        if is_directory(line) or is_ls(line):
            continue

        if is_navigation(line):
            destination = get_navigation_destination(line)
            file_tree.navigate_to(destination)
            continue

        file_size, file_name = line.split(" ")
        file_tree.add_file_to_current_folder(file_name, int(file_size))

    return calculate_size_of_all_folders(file_tree)


def solution_2(input_text: str):
    pass
