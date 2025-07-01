# time complexity: O(n^2)
# space complexity: O(n)

class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        result = []
        total = 1
        i = 0

        while i < n:
            count = 1
            while i + 1 < n and word[i] == word[i + 1]:
                count += 1
                i += 1
            total += (count - 1)
            result.append(f"{count}{word[i]}")
            i += 1

        return total


print(Solution().possibleStringCount("abbcccc"))
print(Solution().possibleStringCount("abcd"))
print(Solution().possibleStringCount("aaaa"))
print(Solution().possibleStringCount("eae"))
