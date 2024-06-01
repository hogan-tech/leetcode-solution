# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def scoreOfString(self, s: str) -> int:
        ASCIIList = []
        result = 0
        for charc in s:
            ASCIIList.append(ord(charc))
        for idx in range(len(s) - 1):
            result += abs(ASCIIList[idx] - ASCIIList[idx + 1])
        return result


s = "hello"
print(Solution().scoreOfString(s))
