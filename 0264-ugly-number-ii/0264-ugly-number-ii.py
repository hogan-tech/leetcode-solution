# time complexity: O(nlogm)
# space complexity: O(m)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNumbersSet = set()
        uglyNumbersSet.add(1)

        currentUgly = 1
        for i in range(n):
            currentUgly = min(uglyNumbersSet)
            uglyNumbersSet.remove(currentUgly)

            uglyNumbersSet.add(currentUgly * 2)
            uglyNumbersSet.add(currentUgly * 3)
            uglyNumbersSet.add(currentUgly * 5)

        return currentUgly


n = 175
print(Solution().nthUglyNumber(n))
