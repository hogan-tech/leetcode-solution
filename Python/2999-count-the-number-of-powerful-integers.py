# time complexity: O(log(finish))
# space complexity: O(log(finish))
class Solution:
    def numberOfPowerfulInt(
        self, start: int, finish: int, limit: int, s: str
    ) -> int:
        startStr = str(start - 1)
        finishStr = str(finish)
        return self.calculate(finishStr, s, limit) - self.calculate(startStr, s, limit)

    def calculate(self, x: str, s: str, limit: int) -> int:
        if len(x) < len(s):
            return 0
        if len(x) == len(s):
            return 1 if x >= s else 0

        suffix = x[len(x) - len(s):]
        count = 0
        preLen = len(x) - len(s)

        for i in range(preLen):
            if limit < int(x[i]):
                count += (limit + 1) ** (preLen - i)
                return count
            count += int(x[i]) * (limit + 1) ** (preLen - 1 - i)

        if suffix >= s:
            count += 1

        return count


start = 1
finish = 6000
limit = 4
s = "124"
print(Solution().numberOfPowerfulInt(start, finish, limit, s))
start = 15
finish = 215
limit = 6
s = "10"
print(Solution().numberOfPowerfulInt(start, finish, limit, s))
start = 1000
finish = 2000
limit = 4
s = "3000"
print(Solution().numberOfPowerfulInt(start, finish, limit, s))
