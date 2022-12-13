class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = {}
        self.children = []

    def add_file(self, name: str, size: int):
        self.files[name] = size


class FileTree:
    def __init__(self) -> None:
        self.__root = Folder("/")
        self.__current_folder = self.__root
        self.__all_folders = [self.__root]

    def navigate_to(self, destination: str):
        if destination == "..":
            self.__current_folder = self.__current_folder.parent
        elif destination == "/":
            self.__current_folder = self.__root
        else:
            folder = self.find_children_in_current_folder(destination)
            if not folder:
                folder = Folder(destination, self.__current_folder)
                self.__current_folder.children.append(folder)
                self.__all_folders.append(folder)

            self.__current_folder = folder

    def find_children_in_current_folder(self, destination: str):
        return next(
            (
                child
                for child in self.__current_folder.children
                if self.__current_folder.name == destination
            ),
            None,
        )

    def add_file_to_current_folder(self, name: str, size: int):
        self.__current_folder.add_file(name, size)

    def get_all_folders(self):
        return self.__all_folders

    def get_root(self):
        return self.__root
