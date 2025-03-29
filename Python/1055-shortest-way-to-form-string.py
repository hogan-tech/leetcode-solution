# time complexity: O(s*t)
# space complexity: O(1)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        sourceCharSet = set(source)
        for char in target:
            if char not in sourceCharSet:
                return -1

        m = len(source)
        sourceIdx = 0
        count = 0
        for char in target:
            if sourceIdx == 0:
                count += 1
            while source[sourceIdx] != char:
                sourceIdx = (sourceIdx + 1) % m
                if sourceIdx == 0:
                    count += 1
            sourceIdx = (sourceIdx + 1) % m
        return count


source = "abc"
target = "abcbc"
print(Solution().shortestWay(source, target))
source = "abc"
target = "acdbc"
print(Solution().shortestWay(source, target))
source = "xyz"
target = "xzyxz"
print(Solution().shortestWay(source, target))
