# time complexity: O(n*m^1/2)
# space complexity: O(n+m)
from collections import defaultdict
from typing import List


class Solution:
    def dfs(self, index, visitedIndex, visitedPrime):
        if visitedIndex[index]:
            return
        visitedIndex[index] = True

        for prime in self.index2prime[index]:
            if visitedPrime.get(prime, False):
                continue
            visitedPrime[prime] = True
            for index1 in self.prime2index[prime]:
                if visitedIndex[index1]:
                    continue
                self.dfs(index1, visitedIndex, visitedPrime)

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        self.prime2index = defaultdict(list)
        self.index2prime = defaultdict(list)
        for i, num in enumerate(nums):
            temp = num
            for j in range(2, int(num ** 0.5) + 1):
                if temp % j == 0:
                    self.prime2index[j].append(i)
                    self.index2prime[i].append(j)
                    while temp % j == 0:
                        temp //= j
            if temp > 1:
                self.prime2index.setdefault(temp, []).append(i)
                self.index2prime.setdefault(i, []).append(temp)

        visitedIndex = [False] * len(nums)
        visitedPrime = {}
        self.dfs(0, visitedIndex, visitedPrime)

        return all(visitedIndex)


nums = [2, 3, 6]
print(Solution().canTraverseAllPairs(nums))
