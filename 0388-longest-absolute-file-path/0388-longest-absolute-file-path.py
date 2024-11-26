# time complexity: O(n^2)
# space complexity: O(n)
from collections import deque


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        items = input.split('\n')
        result = 0
        queue = deque()
        for item in items:
            if not item.startswith('\t'):
                if item.count('.'):
                    result = max(result, len(item))
                queue.appendleft((item, 0, len(item)))
            else:
                level = item.count('\t')
                itemLength = len(item)-level+1
                queue.appendleft((item, level, itemLength))
                temp = 0
                if item.count('.'):
                    currLevel = level
                    temp += itemLength
                    for i in range(1, len(queue)):
                        _, nextLevel, nextLength = queue[i]
                        if nextLevel == currLevel - 1:
                            temp += nextLength
                            currLevel -= 1
                    result = max(result, temp)
        return result


input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(Solution().lengthLongestPath(input))
input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(Solution().lengthLongestPath(input))
input = "a"
print(Solution().lengthLongestPath(input))
input = "file1.txt\nfile2.txt\nlongfile.txt"
print(Solution().lengthLongestPath(input))
