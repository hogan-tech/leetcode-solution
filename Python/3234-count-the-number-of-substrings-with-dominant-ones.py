# time complexity: O(n ^ (1/n))
# space complexity: O(n)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        prefix = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == "0":
                prefix[i + 1] = i
            else:
                prefix[i + 1] = prefix[i]

        result = 0
        for i in range(1, n + 1):
            zeroes = 1 if s[i - 1] == "0" else 0
            j = i
            while j > 0 and zeroes * zeroes <= n:
                ones = (i - prefix[j]) - zeroes
                if zeroes * zeroes <= ones:
                    result += min(j - prefix[j], ones - zeroes * zeroes + 1)
                j = prefix[j]
                zeroes += 1
        return result


s = "00011"
print(Solution().numberOfSubstrings(s))
s = "101101"
print(Solution().numberOfSubstrings(s))
