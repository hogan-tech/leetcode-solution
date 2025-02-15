# time complexity: O(n * 2^log(n))
# space complexity: O(2 ^ log(n))
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def checkValidPartition(strNum, target):
            if not strNum and target == 0:
                return True
            for i in range(len(strNum)):
                left = strNum[:i + 1]
                right = strNum[i + 1:]
                leftNum = int(left)
                if checkValidPartition(right, target - leftNum):
                    return True
            return False

        result = 0
        for i in range(1, n + 1):
            sqrNum = i ** 2
            if checkValidPartition(str(sqrNum), i):
                result += sqrNum
        return result


n = 10
print(Solution().punishmentNumber(n))
n = 37
print(Solution().punishmentNumber(n))
