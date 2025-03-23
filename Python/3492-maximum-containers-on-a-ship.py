# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        n = n ** 2
        return maxWeight // w if maxWeight // w < n else n


n = 20
w = 3
maxWeight = 15
print(Solution().maxContainers(n, w, maxWeight))
n = 3
w = 5
maxWeight = 20
print(Solution().maxContainers(n, w, maxWeight))
