# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def numSteps(self, s: str) -> int:
        carry = 0
        steps = 0
        for i in range(len(s) - 1, 0, -1):
            currNum = int(s[i]) + carry
            if currNum % 2:
                carry = currNum
                steps += 2
            else:
                steps += 1
        return carry + steps


s = "1101"
print(Solution().numSteps(s))
s = "10"
print(Solution().numSteps(s))
s = "1"
print(Solution().numSteps(s))
