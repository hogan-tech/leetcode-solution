class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstIdx = 0
        secondIdx = 0
        result = []
        while firstIdx < len(firstList) and secondIdx < len(secondList):
            start = max(firstList[firstIdx][0], secondList[secondIdx][0])
            end = min(firstList[firstIdx][1], secondList[secondIdx][1])

            if start <= end:
                result.append([start, end])
            
            if firstList[firstIdx][1] < secondList[secondIdx][1]:
                firstIdx += 1
            else:
                secondIdx += 1
        return result