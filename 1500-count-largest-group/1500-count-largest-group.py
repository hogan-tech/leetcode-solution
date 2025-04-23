from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        def getDigitSum(num):
            count = 0
            for c in str(num):
                count += int(c)
            return count
        
        hashSet = defaultdict(list)
        maxLen = 0 
        for num in range(1, n + 1):
            count = getDigitSum(num)
            hashSet[count].append(num)
            maxLen = max(maxLen, len(hashSet[count]))
        
        result = 0
        for value in hashSet.values():
            if len(value) == maxLen:
                result += 1
        return result


n = 46
print(Solution().countLargestGroup(n))
n = 2
print(Solution().countLargestGroup(n))

'''
n = 1 -> 9
return n

n = 10 -> 99
return 

[1,10, 19], [2,11, 20], [3,12,21], [4,13], [5,14], [6,15], [7,16], [8,17], [9,18].
'''