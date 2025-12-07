# time complexity: O(n * 10 ^ (n/2))
# space complexity: O(n)
class Solution:
    def completePrime(self, num: int) -> bool:
        def isPrime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        s = str(num)
        n = len(s)
        for k in range(1, n + 1):
            prefixVal = int(s[:k])
            if not isPrime(prefixVal):
                return False
        for k in range(n):
            suffixVal = int(s[k:])
            if not isPrime(suffixVal):
                return False
        return True


num = 23
print(Solution().completePrime(num))
num = 39
print(Solution().completePrime(num))
num = 7
print(Solution().completePrime(num))
