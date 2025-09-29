# time complexity: O(n)
# space complexity: O(n)
from collections import Counter, defaultdict


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        freqMap = defaultdict(list)
        for char, count in Counter(s).items():
            freqMap[count].append(char)

        result = ""
        maxSize = 0
        maxFreq = 0
        for count, group in freqMap.items():
            size = len(group)
            if size > maxSize or (size == maxSize and count > maxFreq):
                maxSize = size
                maxFreq = count
                result = "".join(group)
        return result


s = "aaabbbccdddde"
print(Solution().majorityFrequencyGroup(s))
s = "abcd"
print(Solution().majorityFrequencyGroup(s))
s = "pfpfgi"
print(Solution().majorityFrequencyGroup(s))
s = "asrhyrmzhcehcydmrmce"
print(Solution().majorityFrequencyGroup(s))
