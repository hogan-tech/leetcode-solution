# time complexity: O(n^2)
# space complexity: O(1)
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        result = 0
        for i in range(len(s)):
            vowels = 0
            consonants = 0
            for j in range(i, len(s)):
                if s[j] in ['a', 'e', 'i', 'o', 'u']:
                    vowels += 1
                else:
                    consonants += 1
                if vowels == consonants and (vowels * consonants) % k == 0:
                    result += 1

        return result


s = "uzuxpzou"
k = 3
print(Solution().beautifulSubstrings(s, k))
s = "baeyh"
k = 2
print(Solution().beautifulSubstrings(s, k))
s = "abba"
k = 1
print(Solution().beautifulSubstrings(s, k))
s = "bcdf"
k = 1
print(Solution().beautifulSubstrings(s, k))
