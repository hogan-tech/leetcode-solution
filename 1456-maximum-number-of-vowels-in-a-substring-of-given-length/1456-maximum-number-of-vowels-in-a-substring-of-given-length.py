# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        sList = [0] * len(s)
        for i in range(len(s)):
            if s[i] in vowels:
                sList[i] += 1
        tempSum = 0
        result = 0
        for i in range(k):
            tempSum += sList[i]
        result = tempSum
        for i in range(k, len(s)):
            tempSum += sList[i] - sList[i - k]
            result = max(tempSum, result)
        return result


s = "aeiou"
k = 2
print(Solution().maxVowels(s, k))
