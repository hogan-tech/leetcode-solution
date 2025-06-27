from collections import deque
from typing import Counter


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        candidates = [c for c, count in freq.items() if count >= k]
        candidates.sort(reverse=True)

        result = ""
        queue = deque(candidates)

        def isSubseq(subseq: str) -> bool:
            it = iter(s)
            for ch in subseq * k:
                if ch not in it:
                    return False
            return True

        while queue:
            curr = queue.popleft()
            if len(curr) > len(result) or (len(curr) == len(result) and curr > result):
                result = curr
            for ch in candidates:
                nextSeq = curr + ch
                if isSubseq(nextSeq):
                    queue.append(nextSeq)
        return result


s = "letsleetcode"
k = 2
print(Solution().longestSubsequenceRepeatedK(s, k))
s = "bb"
k = 2
print(Solution().longestSubsequenceRepeatedK(s, k))
s = "ab"
k = 2
print(Solution().longestSubsequenceRepeatedK(s, k))
