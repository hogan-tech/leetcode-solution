# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        subsetCompaniesIdx = set()
        for i in range(len(favoriteCompanies)):
            for j in range(len(favoriteCompanies)):
                if i == j:
                    continue
                if set(favoriteCompanies[j]).issubset(set(favoriteCompanies[i])):
                    subsetCompaniesIdx.add(j)
        result = [num for num in range(
            len(favoriteCompanies)) if num not in subsetCompaniesIdx]
        return result


favoriteCompanies = [["leetcode", "google", "facebook"],
                     ["google", "microsoft"],
                     ["google", "facebook"],
                     ["google"],
                     ["amazon"]]
print(Solution().peopleIndexes(favoriteCompanies))
favoriteCompanies = [["leetcode", "google", "facebook"],
                     ["leetcode", "amazon"], ["facebook", "google"]]
print(Solution().peopleIndexes(favoriteCompanies))
favoriteCompanies = [["leetcode"], ["google"], ["facebook"], ["amazon"]]
print(Solution().peopleIndexes(favoriteCompanies))
