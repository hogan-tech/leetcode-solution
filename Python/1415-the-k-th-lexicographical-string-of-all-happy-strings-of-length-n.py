# time complexity: O(n*2^n)
# space complexity: O(2^n)
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        def backtrack(comb):
            if len(comb) == n:
                result.append(list(comb))
                return
            for c in ['a', 'b', 'c']:
                if len(comb) > 0 and c == comb[-1]:
                    continue

                comb.append(c)
                backtrack(comb)
                comb.pop()
        backtrack([])
        if len(result) < k:
            return ""
        return ''.join(result[k - 1])


n = 1
k = 3
print(Solution().getHappyString(n, k))
n = 1
k = 4
print(Solution().getHappyString(n, k))
n = 3
k = 9
print(Solution().getHappyString(n, k))
