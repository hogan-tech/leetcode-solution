# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        if num < k:
            return -1
        temp = num % 10
        for i in range(1, 11):
            if (i*k) % 10 == temp:
                if i*k <= num:
                    return i
        return -1


'''
9 * answer + 10 * xxx = num
-> num % 10 == 9 * answer % 10

0:[0]
1:[1,2,3,4,5,6,7,8,9,0]
2:[2,4,8,6,0]
3:[3,6,9,2,5,8,1,4,7,0]
4:[4,8,2,6,0]
5:[5,0]
6:[6,2,8,4,0]
7:[7,4,1,8,5,2,9,6,3,0]
8:[8,6,4,2,0]
9:[9,8,7,6,5,4,3,2,1,0]

'''
num = 58
k = 9
print(Solution().minimumNumbers(num, k))
num = 37
k = 2
print(Solution().minimumNumbers(num, k))
num = 0
k = 7
print(Solution().minimumNumbers(num, k))
num = 1
k = 1
print(Solution().minimumNumbers(num, k))
