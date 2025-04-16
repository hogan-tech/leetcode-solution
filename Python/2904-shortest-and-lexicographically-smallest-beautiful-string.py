# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        left = 0
        right = 0
        count = 0
        result = ""
        while right < n:
            if s[right] == '1':
                count += 1
            if count == k:
                while left < n and count == k:
                    temp = s[left:right + 1]
                    if not result or len(result) > len(temp):
                        result = temp
                    elif len(result) == len(temp):
                        result = min(result, temp)
                    if s[left] == '1':
                        count -= 1
                    left += 1
            right += 1
        return result


s = "100011001"
k = 3
print(Solution().shortestBeautifulSubstring(s, k))
s = "1011"
k = 2
print(Solution().shortestBeautifulSubstring(s, k))
s = "000"
k = 1
print(Solution().shortestBeautifulSubstring(s, k))
s = "111111110010001010"
k = 11
print(Solution().shortestBeautifulSubstring(s, k))
s = "1100001110111100100"
k = 8
print(Solution().shortestBeautifulSubstring(s, k))
