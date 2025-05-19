# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        result = ""
        for c in s:
            if k == 0:
                result += c
                continue
            fromLeft = ord(c) - ord('a')
            fromRight = ord('a') + 26 - ord(c)
            minDistance = min(fromLeft, fromRight)
            if k >= minDistance:
                k -= minDistance
                result += 'a'
            elif k < minDistance:
                result += chr(ord(c) - k)
                k = 0
        return result


'''
ord(c) - ord('a') -> a:0, b:1, c:2 ..... z:26, a: 27
'''
s = "zbbz"
k = 3
print(Solution().getSmallestString(s, k))
s = "xaxcd"
k = 4
print(Solution().getSmallestString(s, k))
s = "lol"
k = 0
print(Solution().getSmallestString(s, k))
