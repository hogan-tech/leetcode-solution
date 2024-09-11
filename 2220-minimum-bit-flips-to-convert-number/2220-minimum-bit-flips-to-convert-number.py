

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        startBin = bin(start)[2:]
        goalBin = bin(goal)[2:]
        diffLen = abs(len(startBin) - len(goalBin))
        if len(startBin) > len(goalBin):
            goalBin = "0" * diffLen + goalBin
        else:
            startBin = "0" * diffLen + startBin
        for i in range(len(startBin)):
            if goalBin[i] != startBin[i]:
                count += 1
        print(startBin)
        print(goalBin)
        return count

start = 3
goal = 4
print(Solution().minBitFlips(start, goal))
