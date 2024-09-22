# time complexity: O(logn ^ 2)
# space complexity: O(1)
class Solution(object):
    def findKthNumber(self, n, k):
        curr = 1
        k -= 1

        while k > 0:
            step = self.countSteps(n, curr, curr + 1)
            if step <= k:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1

        return curr

    def countSteps(self, n, prefix1, prefix2):
        steps = 0
        while prefix1 <= n:
            steps += min(n + 1, prefix2) - prefix1
            prefix1 *= 10
            prefix2 *= 10
        return steps


n = 13
k = 2
print(Solution().findKthNumber(n, k))
