from collections import defaultdict


class FileSystem:

    def __init__(self):
        self.paths = defaultdict()

    def createPath(self, path: str, value: int) -> bool:

        if path == "/" or len(path) == 0 or path in self.paths:
            return False

        parent = path[:path.rfind('/')]
        if len(parent) > 1 and parent not in self.paths:
            return False

        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)
