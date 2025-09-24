# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total


s = "III"
print(Solution().romanToInt(s))
s = "LVIII"
print(Solution().romanToInt(s))
s = "MCMXCIV"
print(Solution().romanToInt(s))
