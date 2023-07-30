from sortedcontainers import SortedDict


class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map:
            self.map[key] = SortedDict()
        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""
        
        it = self.map[key].bisect_right(timestamp)
        if it == 0:
            return ""

        return self.map[key].peekitem(it - 1)[1]