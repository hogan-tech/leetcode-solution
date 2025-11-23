# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def minimumFlips(self, n: int) -> int:
        original = bin(n)[2:]
        reverse = original[::-1]
        count = 0
        for i in range(len(original)):
            if original[i] != reverse[i]:
                count += 1
        return count


n = 7
print(Solution().minimumFlips(n))
n = 10
print(Solution().minimumFlips(n))
