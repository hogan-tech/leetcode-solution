# time complexity: O(n^2)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        reponseSet = []
        for row in responses:
            reponseSet.append(set(row))
        reponseHashSet = defaultdict(int)
        for eachSet in reponseSet:
            for reponse in eachSet:
                reponseHashSet[reponse] += 1

        maxFreq = 0
        result = ""
        for response, freq in reponseHashSet.items():
            if freq > maxFreq or (freq == maxFreq and response < result):
                maxFreq = freq
                result = response
        return result


responses = [["good", "ok", "good", "ok"], [
    "ok", "bad", "good", "ok", "ok"], ["good"], ["bad"]]
print(Solution().findCommonResponse(responses))
responses = [["good", "ok", "good"], ["ok", "bad"],
             ["bad", "notsure"], ["great", "good"]]
print(Solution().findCommonResponse(responses))
