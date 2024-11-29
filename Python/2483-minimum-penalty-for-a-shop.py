
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curPenalty = minPenalty = customers.count('Y')
        earliestHour = 0
        for i, ch in enumerate(customers):
            if ch == 'Y':
                curPenalty -= 1
            else:
                curPenalty += 1
            if curPenalty < minPenalty:
                earliestHour = i + 1
                minPenalty = curPenalty
        return earliestHour


customers = "YYNY"

print(Solution().bestClosingTime(customers))
