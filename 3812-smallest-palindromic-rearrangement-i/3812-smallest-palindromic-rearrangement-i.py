# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        mid = ""
        result = ""
        for i, num in enumerate(freq):
            if num % 2 == 1:
                mid = chr(i + ord('a'))
                freq[i] -= 1
            result += chr(i + ord('a')) * (num // 2)

        return result + mid + result[::-1]


s = "z"
print(Solution().smallestPalindrome(s))
s = "babab"
print(Solution().smallestPalindrome(s))
s = "daccad"
print(Solution().smallestPalindrome(s))
