# time complexity: O(nklogn)
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

# time complexity: O(nk)
# space complexity: O(nk)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return list(result.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
strs = [""]
print(Solution().groupAnagrams(strs))
strs = ["a"]
print(Solution().groupAnagrams(strs))
