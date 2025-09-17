# time complexity:
# ls: O(D + K log K)
# mkdir: O(D)
# addContentToFile: O(D + L)
# readContentFromFile: O(D + L)
# space complexity: O(N + T)
# N = number of directories/files
# T = total length of all file contents
from typing import List


class FileSystem:
    class Dir:
        def __init__(self):
            self.dirs = {}
            self.files = {}

    def __init__(self):
        self.root = self.Dir()

    def ls(self, path: str) -> List[str]:
        root = self.root
        files = []
        if path != "/":
            d = path.split("/")
            for i in range(1, len(d) - 1):
                root = root.dirs[d[i]]
            if d[-1] in root.files:
                files.append(d[-1])
                return files
            else:
                root = root.dirs[d[-1]]

        files.extend(root.dirs.keys())
        files.extend(root.files.keys())
        files.sort()
        return files

    def mkdir(self, path: str) -> None:
        root = self.root
        d = path.split("/")
        for i in range(1, len(d)):
            if d[i] not in root.dirs:
                root.dirs[d[i]] = self.Dir()
            root = root.dirs[d[i]]

    def addContentToFile(self, filePath: str, content: str) -> None:
        root = self.root
        d = filePath.split("/")
        for i in range(1, len(d) - 1):
            root = root.dirs[d[i]]
        if d[-1] not in root.files:
            root.files[d[-1]] = ""
        root.files[d[-1]] += content

    def readContentFromFile(self, filePath: str) -> str:
        root = self.root
        d = filePath.split("/")
        for i in range(1, len(d) - 1):
            root = root.dirs[d[i]]

        return root.files[d[-1]]


fileSystem = FileSystem()
print(fileSystem.ls("/"))
fileSystem.mkdir("/a/b/c")
fileSystem.addContentToFile("/a/b/c/d", "hello")
print(fileSystem.ls("/"))
print(fileSystem.readContentFromFile("/a/b/c/d"))
