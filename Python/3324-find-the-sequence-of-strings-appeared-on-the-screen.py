# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        result = []
        current = ''

        for char in target:
            if len(current) == 0 or char != 'a' or target != current:
                current += 'a'
                result.append(current)

            while current[-1] != char and result[-1] != target:
                current = current[:-1] + \
                    chr(((ord(current[-1]) - ord('a') + 1) % 26) + ord('a'))
                result.append(current)

        return result


target = "abc"
print(Solution().stringSequence(target))
target = "aaaaaa"
print(Solution().stringSequence(target))
target = "he"
print(Solution().stringSequence(target))
