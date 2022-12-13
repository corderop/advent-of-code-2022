from utils import (
    calculate_folder_size,
    calculate_size_of_all_folders,
    get_navigation_destination,
    is_directory,
    is_ls,
    is_navigation,
)
from file_tree import FileTree


def solution_1(input_text: str):
    MAX_FOLDER_SIZE = 100000

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

    return calculate_size_of_all_folders(file_tree, MAX_FOLDER_SIZE)


def solution_2(input_text: str):
    FILE_SYSTEM_SIZE = 70000000
    NEEDED_SPACE = 30000000

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

    folders = file_tree.get_all_folders()
    sizes = [calculate_folder_size(folder) for folder in folders]
    sizes.sort()

    used_space = calculate_folder_size(file_tree.get_root())
    for size in sizes:
        remaining_space = FILE_SYSTEM_SIZE - (used_space - size)
        if remaining_space > NEEDED_SPACE:
            return size
