# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        openBrackets = []
        unlocked = []
        for i in range(len(s)):
            if locked[i] == '0':
                unlocked.append(i)
            elif s[i] == '(':
                openBrackets.append(i)
            elif s[i] == ')':
                if openBrackets:
                    openBrackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        while unlocked and openBrackets and openBrackets[-1] < unlocked[-1]:
            unlocked.pop()
            openBrackets.pop()

        if openBrackets:
            return False
        return True


s = "))()))"
locked = "010100"
print(Solution().canBeValid(s, locked))
s = "()()"
locked = "0000"
print(Solution().canBeValid(s, locked))
s = ")"
locked = "0"
print(Solution().canBeValid(s, locked))
