# time complexity: O(nlogn)
# space complexity: O(n)
from collections import defaultdict


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set(["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"])
        vowelMap = defaultdict(int)

        for char in s:
            if char in vowels:
                vowelMap[char] += 1
        if not vowelMap:
            return s
        sortedVowels = sorted(vowelMap.keys(), key=lambda x: ord(x))
        vowelIdx = 0
        result = ""
        for char in s:
            if char not in vowels:
                result += char
            else:
                vowelMap[sortedVowels[vowelIdx]] -= 1
                result += sortedVowels[vowelIdx]
                if vowelMap[sortedVowels[vowelIdx]] == 0:
                    del vowelMap[sortedVowels[vowelIdx]]
                    vowelIdx += 1

        return result


s = "lEetcOde"
print(Solution().sortVowels(s))
s = "lYmpH"
print(Solution().sortVowels(s))
