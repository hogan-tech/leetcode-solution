from typing import List


class FileSystem:
    class Dir:
        def __init__(self):
            self.dirs = {}
            self.files = {}

    def __init__(self):
        self.root = self.Dir()

    def ls(self, path: str) -> List[str]:
        t = self.root
        files = []
        if path != "/":
            d = path.split("/")
            for i in range(1, len(d) - 1):
                t = t.dirs[d[i]]
            if d[-1] in t.files:
                files.append(d[-1])
                return files
            else:
                t = t.dirs[d[-1]]

        files.extend(t.dirs.keys())
        files.extend(t.files.keys())
        files.sort()
        return files

    def mkdir(self, path: str) -> None:
        t = self.root
        d = path.split("/")
        for i in range(1, len(d)):
            if d[i] not in t.dirs:
                t.dirs[d[i]] = self.Dir()
            t = t.dirs[d[i]]

    def addContentToFile(self, filePath: str, content: str) -> None:
        t = self.root
        d = filePath.split("/")
        for i in range(1, len(d) - 1):
            t = t.dirs[d[i]]
        if d[-1] not in t.files:
            t.files[d[-1]] = ""
        t.files[d[-1]] += content

    def readContentFromFile(self, filePath: str) -> str:
        t = self.root
        d = filePath.split("/")
        for i in range(1, len(d) - 1):
            t = t.dirs[d[i]]

        return t.files[d[-1]]


fileSystem = FileSystem()
print(fileSystem.ls("/"))
fileSystem.mkdir("/a/b/c")
fileSystem.addContentToFile("/a/b/c/d", "hello")
print(fileSystem.ls("/"))
print(fileSystem.readContentFromFile("/a/b/c/d"))
