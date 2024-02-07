# time complexity: O(nlogn)
# space complexity: O(k)
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        newList = []
        for letter, freq in counts.most_common():
            newList.append(letter * freq)
        return "".join(newList)


s = "loveleetcode"
print(Solution().frequencySort(s))
