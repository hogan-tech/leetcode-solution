# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibList = [1, 2]

        while fibList[-1] < k:
            fibList.append(fibList[-1] + fibList[-2])
            
        result = 0
        while k > 0:
            while fibList[-1] > k:
                fibList.pop()
            else:
                result += 1
                k -= fibList[-1]
        return result


k = 5
print(Solution().findMinFibonacciNumbers(k))
k = 7
print(Solution().findMinFibonacciNumbers(k))
k = 10
print(Solution().findMinFibonacciNumbers(k))
k = 19
print(Solution().findMinFibonacciNumbers(k))
