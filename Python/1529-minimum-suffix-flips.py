# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def minFlips(self, target: str) -> int:
        prev = '0'
        count = 0
        for c in target:
            if c != prev:
                prev = c
                count += 1
        return count


target = "10111"
print(Solution().minFlips(target))
target = "101"
print(Solution().minFlips(target))
target = "00000"
print(Solution().minFlips(target))
