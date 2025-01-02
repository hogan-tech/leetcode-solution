# time complexity: O(m^n * n)
# space complexity: O(m*n)
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(segment: List[str]):
            segmentLen = len(segment)
            if segmentLen > 3:
                return False
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1
        
        def updateSegments(s: str, currDot: int, segments: List[str], result: List[str]):
            segment = s[currDot + 1:len(s)]
            if valid(segment):
                segments.append(segment)
                result.append('.'.join(segments))
                segments.pop()

        def backtrack(s: str, prevDot: int, dots: int, segments: List[str], result: List[str]):
            size = len(s)

            for currDot in range(prevDot + 1, min(size - 1, prevDot + 4)):
                segment = s[prevDot + 1: currDot + 1]
                if valid(segment):
                    segments.append(segment)

                    if dots - 1 == 0:
                        updateSegments(s, currDot, segments, result)
                    else:
                        backtrack(s, currDot, dots-1, segments, result)
                    
                    segments.pop()

            return
        result = []
        segments = []
        backtrack(s, -1, 3, segments, result)
        return result


s = "25525511135"
print(Solution().restoreIpAddresses(s))
