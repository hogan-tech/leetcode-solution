# time complexity: O(n+q)
# space complexity: O(n)
from typing import List


class Solution:
    def sameEndSubstringCount(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        n = len(s)
        charFreqPrefixSum = [[0] * n for _ in range(26)]
        for i, char in enumerate(s):
            charFreqPrefixSum[ord(char) - ord("a")][i] += 1
        for freq in charFreqPrefixSum:
            for j in range(1, n):
                freq[j] += freq[j - 1]
        results = []
        for left, right in queries:
            countSameEndSubstrings = 0
            for freq in charFreqPrefixSum:
                leftFreq = 0 if left == 0 else freq[left - 1]
                rightFreq = freq[right]
                frequencyInRange = rightFreq - leftFreq
                countSameEndSubstrings += (
                    frequencyInRange * (frequencyInRange + 1) // 2
                )
            results.append(countSameEndSubstrings)

        return results


s = "abcaab"
queries = [[0, 0], [1, 4], [2, 5], [0, 5]]
print(Solution().sameEndSubstringCount(s, queries))
