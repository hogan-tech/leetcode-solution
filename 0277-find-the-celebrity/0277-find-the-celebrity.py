# time complexity: O(n)
# space complexity: O(1)
graph = [[1, 1, 0], [0, 1, 0], [1, 1, 1]]


def knows(a: int, b: int) -> bool:
    return graph[a][b] == 1


class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n = n
        celebrity_candidate = 0
        for i in range(1, n):
            if knows(celebrity_candidate, i):
                celebrity_candidate = i
        if self.isCelebrity(celebrity_candidate):
            return celebrity_candidate
        return -1

    def isCelebrity(self, i):
        for j in range(self.n):
            if i == j:
                continue
            if knows(i, j) or not knows(j, i):
                return False
        return True


print(Solution().findCelebrity(3))
