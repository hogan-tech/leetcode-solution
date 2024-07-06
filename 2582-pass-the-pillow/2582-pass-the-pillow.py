# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def passThePillow(self, n, time):
        fullRounds = time // (n - 1)
        extraTime = time % (n - 1)
        if fullRounds % 2 == 0:
            return extraTime + 1
        else:
            return n - extraTime


n = 3
time = 2
print(Solution().passThePillow(n, time))
