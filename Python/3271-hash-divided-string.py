# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        numList = []
        result = ""
        for c in s:
            numList.append(ord(c) - ord('a'))
        for i in range(0, len(numList), k):
            currSum = sum(numList[i:i + k]) % 26
            result += chr(ord('a') + currSum)
        return result


s = "abcd"
k = 2
print(Solution().stringHash(s, k))
s = "mxz"
k = 3
print(Solution().stringHash(s, k))
