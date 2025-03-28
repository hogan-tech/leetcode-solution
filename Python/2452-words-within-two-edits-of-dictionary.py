# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def validDiff(query, diction):
            count = 0
            for i in range(len(query)):
                if query[i] != diction[i]:
                    count += 1
            return count <= 2

        result = []
        for query in queries:
            flag = False
            for diction in dictionary:
                if flag:
                    continue
                if validDiff(query, diction):
                    result.append(query)
                    flag = True
                    continue

        return result


queries = ["word", "note", "ants", "wood"]
dictionary = ["wood", "joke", "moat"]
print(Solution().twoEditWords(queries, dictionary))
queries = ["yes"]
dictionary = ["not"]
print(Solution().twoEditWords(queries, dictionary))
