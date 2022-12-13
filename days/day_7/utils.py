from file_tree import FileTree


def calculate_size_of_all_folders(file_tree: FileTree):
    total_size = 0
    all_folders = file_tree.get_all_folders()

    for folder in all_folders:
        try:
            size = calculate_folder_size(folder)
            total_size += size
        except Exception:
            pass  # More than 100000

    return total_size


def calculate_folder_size(folder, max_size=100000):
    size = sum(folder.files.values())

    if size > max_size:
        raise Exception("Too big")

    for child in folder.children:
        size += calculate_folder_size(child, max_size - size)

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
