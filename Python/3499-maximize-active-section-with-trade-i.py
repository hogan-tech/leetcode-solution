# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        onesCount = s.count('1')

        oneArr = []
        i = 0
        lenT = len(t)
        while i < lenT:
            if t[i] == '1':
                start = i
                while i < lenT and t[i] == '1':
                    i += 1
                if start > 0 and i < lenT and t[start - 1] == '0' and t[i] == '0':
                    length = i - start
                    leftZeroStart = start - 1
                    while leftZeroStart >= 0 and t[leftZeroStart] == '0':
                        leftZeroStart -= 1
                    leftZeros = start - 1 - leftZeroStart

                    rightZeroEnd = i
                    while rightZeroEnd < lenT and t[rightZeroEnd] == '0':
                        rightZeroEnd += 1
                    rightZeros = rightZeroEnd - i
                    oneArr.append((length, leftZeros, rightZeros))
            else:
                i += 1

        if not oneArr:
            return onesCount

        zeroArr = []
        maxZero = secondMaxZero = thirdMaxZero = 0
        i = 0
        while i < lenT:
            if t[i] == '0':
                start = i
                while i < lenT and t[i] == '0':
                    i += 1

                if start > 0 and i < lenT and t[start - 1] == '1' and t[i] == '1':
                    length = i - start
                    zeroArr.append(length)
                    if length > maxZero:
                        thirdMaxZero = secondMaxZero
                        secondMaxZero = maxZero
                        maxZero = length
                    elif length > secondMaxZero:
                        thirdMaxZero = secondMaxZero
                        secondMaxZero = length
                    elif length > thirdMaxZero:
                        thirdMaxZero = length
            else:
                i += 1

        maxGain = 0
        for L, leftZeros, rightZeros in oneArr:
            newZeroBlock = leftZeros + L + rightZeros
            candidates = [newZeroBlock]
            if zeroArr:
                if maxZero != leftZeros and maxZero != rightZeros:
                    candidates.append(maxZero)
                elif secondMaxZero != leftZeros and secondMaxZero != rightZeros:
                    candidates.append(secondMaxZero)
                else:
                    candidates.append(thirdMaxZero)
            M = max(candidates)
            currentGain = M - L
            if currentGain > maxGain:
                maxGain = currentGain

        return onesCount + maxGain if maxGain > 0 else onesCount


s = "01"
print(Solution().maxActiveSectionsAfterTrade(s))
s = "0100"
print(Solution().maxActiveSectionsAfterTrade(s))
s = "1000100"
print(Solution().maxActiveSectionsAfterTrade(s))
s = "01010"
print(Solution().maxActiveSectionsAfterTrade(s))
