# time complexity: O(d! * d)
# space complexity: O(d)
from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def backtrack(comb, counter):
            if len(comb) == len(nums) and comb[0] != '0':
                result.append(int(''.join(comb)))
                return

            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[num] += 1
        nums = []
        result = []
        for c in str(n):
            nums.append(c)
        backtrack([], Counter(nums))
        for num in result:
            if bin(num).count('1') == 1:
                print(num)
                return True

        return False


n = 1
print(Solution().reorderedPowerOf2(n))
n = 10
print(Solution().reorderedPowerOf2(n))
n = 46
print(Solution().reorderedPowerOf2(n))
n = 56635
print(Solution().reorderedPowerOf2(n))
