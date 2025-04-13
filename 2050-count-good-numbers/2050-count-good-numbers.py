# time complexity: O(logn)
# space complexity: O(1)
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        def quickPow(x: int, y: int) -> int:
            result = 1
            multi = x
            while y > 0:
                if y % 2 == 1:
                    result = result * multi % MOD
                multi = multi * multi % MOD
                y //= 2
            return result

        return quickPow(5, (n + 1) // 2) * quickPow(4, n // 2) % MOD


'''
n = 1
5
0 2 4 6 8

n = 4
5 * 4 * 5 * 4
2 4 6 8

2 3 5 7

0 2 4 6 8

2 3 5 7
'''
n = 1
print(Solution().countGoodNumbers(n))
n = 4
print(Solution().countGoodNumbers(n))
n = 50
print(Solution().countGoodNumbers(n))
