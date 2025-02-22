# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        result = 0
        pens = total // cost1
        for pen in range(pens + 1):
            pencil = (total - pen * cost1) // cost2
            result += pencil + 1
        return result


total = 20
cost1 = 10
cost2 = 5
print(Solution().waysToBuyPensPencils(total, cost1, cost2))
total = 5
cost1 = 10
cost2 = 10
print(Solution().waysToBuyPensPencils(total, cost1, cost2))

'''
pen * cost1 + pencil * cost2 = total
pencil = (total - pen * cost1) / cost2
'''
