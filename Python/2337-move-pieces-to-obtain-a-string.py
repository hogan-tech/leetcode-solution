# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        startIdx = 0
        targetIdx = 0
        while startIdx < n or targetIdx < n:

            while startIdx < n and start[startIdx] == "_":
                startIdx += 1
            while targetIdx < n and target[targetIdx] == "_":
                targetIdx += 1

            if startIdx == n or targetIdx == n:
                return startIdx == n and targetIdx == n

            if start[startIdx] != target[targetIdx]:
                return False
            if start[startIdx] == "R" and startIdx > targetIdx:
                return False
            if start[startIdx] == "L" and startIdx < targetIdx:
                return False

            startIdx += 1
            targetIdx += 1
        return True


start = "_L__R__R_"
target = "L______RR"
print(Solution().canChange(start, target))
start = "R_L_"
target = "__LR"
print(Solution().canChange(start, target))
start = "_R"
target = "R_"
print(Solution().canChange(start, target))
