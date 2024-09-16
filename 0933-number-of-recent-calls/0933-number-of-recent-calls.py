# time complexity: O(1)
# space complexity: O(1)
from collections import deque


class RecentCounter:

    def __init__(self):
        self.slidingWindow = deque()

    def ping(self, t: int) -> int:
        self.slidingWindow.append(t)

        while self.slidingWindow[0] < t - 3000:
            self.slidingWindow.popleft()

        return len(self.slidingWindow)
