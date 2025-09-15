# time complexity: O(nlogn * n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            wordMap[key].append(word)
        return [row for row in wordMap.values()]


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
strs = [""]
print(Solution().groupAnagrams(strs))
strs = ["a"]
print(Solution().groupAnagrams(strs))
