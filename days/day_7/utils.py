from file_tree import FileTree


def calculate_size_of_all_folders(file_tree: FileTree, max_folder_size: int):
    total_size = 0
    all_folders = file_tree.get_all_folders()

    for folder in all_folders:
        size = calculate_folder_size(folder)
        if size < max_folder_size:
            total_size += size

    return total_size


def calculate_folder_size(folder):
    size = sum(folder.files.values())

    for child in folder.children:
        size += calculate_folder_size(child)

    return size


def is_ls(line):
    return line.startswith("$ ls")


def is_directory(line):
    return line.startswith("dir ")


def is_navigation(line):
    return line.startswith("$ cd")


def get_navigation_destination(line):
    return line.split(" ")[-1]


def is_command(line: str):
    return line.startswith("$ ")
