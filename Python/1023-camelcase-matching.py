# time complexity: O(n^2)
# space complexity: O(n)
from typing import Counter, List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        result = []
        for query in queries:
            left = 0
            right = 0
            while left < len(query) and right < len(pattern):
                if query[left] == pattern[right]:
                    left += 1
                    right += 1
                else:
                    left += 1

            if right == len(pattern) and all(map(str.islower, Counter(query) - Counter(pattern))):
                result.append(True)
            else:
                result.append(False)

        return result


queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
pattern = "FB"
print(Solution().camelMatch(queries, pattern))
queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
pattern = "FoBa"
print(Solution().camelMatch(queries, pattern))
queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
pattern = "FoBaT"
print(Solution().camelMatch(queries, pattern))
