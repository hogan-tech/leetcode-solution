# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        result = zeros = 0

        for i in range(len(s)):
            zeros += 1 if s[i] == "0" else 0

            if s[i] == "1" and zeros:
                result = max(result+1, zeros)

        return result


s = "0110101"
print(Solution().secondsToRemoveOccurrences(s))
s = "11100"
print(Solution().secondsToRemoveOccurrences(s))
s = "001011"
print(Solution().secondsToRemoveOccurrences(s))
'''
001011
010101
101010
110100
111000
'''
