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
        l = 0
        ans = ""
        for char in s:
            if char not in vowels:
                ans += char
            else:
                vowelMap[sortedVowels[l]] -= 1
                ans += sortedVowels[l]
                if vowelMap[sortedVowels[l]] == 0:
                    del vowelMap[sortedVowels[l]]
                    l += 1

        return ans


s = "lEetcOde"
print(Solution().sortVowels(s))
