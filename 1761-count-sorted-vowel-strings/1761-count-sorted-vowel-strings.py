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

n = 1
print(Solution().countVowelStrings(n))
n = 33
print(Solution().countVowelStrings(n))
