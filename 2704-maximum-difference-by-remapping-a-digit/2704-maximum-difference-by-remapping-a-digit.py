class Solution:
    def minMaxDifference(self, num: int) -> int:
        maxNumList = [c for c in str(num)]
        minNumList = [c for c in str(num)]
        maxFind = False
        minFind = False
        maxNum = ''
        minNum = ''
        for i in range(len(maxNumList)):
            if maxNumList[i] != '9' and not maxFind:
                maxNum = maxNumList[i]
                maxFind = True
            if maxFind and maxNumList[i] == maxNum:
                maxNumList[i] = '9'
            if minNumList[i] != '0' and not minFind:
                minNum = minNumList[i]
                minFind = True
            if minFind and minNumList[i] == minNum:
                minNumList[i] = '0'

        maxNum = int(''.join(maxNumList))
        minNum = int(''.join(minNumList))

        return maxNum - minNum


'''
1 -> 9
99899
1 -> 0
00890


'''
num = 11891
print(Solution().minMaxDifference(num))
num = 90
print(Solution().minMaxDifference(num))
