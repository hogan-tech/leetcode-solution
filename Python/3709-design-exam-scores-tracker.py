# time complexity: O(logn)
# space complexity: O(n)
from bisect import bisect_left, bisect_right


class ExamTracker:

    def __init__(self):
        self.times = []
        self.prefix = []

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        if not self.prefix:
            self.prefix.append(score)
        else:
            self.prefix.append(self.prefix[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        left = bisect_left(self.times, startTime)
        right = bisect_right(self.times, endTime) - 1

        if left > right:
            return 0

        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]


examTracker = ExamTracker()
examTracker.record(1, 98)
print(examTracker.totalScore(1, 1))
examTracker.record(5, 99)
print(examTracker.totalScore(1, 3))
print(examTracker.totalScore(1, 5))
print(examTracker.totalScore(3, 4))
print(examTracker.totalScore(2, 5))
