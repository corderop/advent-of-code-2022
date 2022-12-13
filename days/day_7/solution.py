from utils import (
    calculate_folder_size,
    calculate_size_of_all_folders,
    process_commands_into_file_tree,
)
from file_tree import FileTree


def solution_1(input_text: str):
    MAX_FOLDER_SIZE = 100000

    lines = input_text.splitlines()
    file_tree = process_commands_into_file_tree(lines)
    return calculate_size_of_all_folders(file_tree, MAX_FOLDER_SIZE)


def solution_2(input_text: str):
    FILE_SYSTEM_SIZE = 70000000
    NEEDED_SPACE = 30000000

    lines = input_text.splitlines()
    file_tree = process_commands_into_file_tree(lines)

    folders = file_tree.get_all_folders()
    sizes = [calculate_folder_size(folder) for folder in folders]
    sizes.sort()

    used_space = calculate_folder_size(file_tree.get_root())
    for size in sizes:
        remaining_space = FILE_SYSTEM_SIZE - (used_space - size)
        if remaining_space > NEEDED_SPACE:
            return size
