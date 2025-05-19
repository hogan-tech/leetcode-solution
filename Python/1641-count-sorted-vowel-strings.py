# s)
class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        result = []

        def backtrack(curr: str):
            if len(curr) == n:
                result.append(curr)
                return
            for vowel in vowels:
                if len(curr) == 0 or vowel >= curr[-1]:
                    curr += vowel
                    backtrack(curr)
                    curr = curr[:-1]
        backtrack("")
        return len(result)

# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24


n = 1
print(Solution().countVowelStrings(n))
n = 33
print(Solution().countVowelStrings(n))
