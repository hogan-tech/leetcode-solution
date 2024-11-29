from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        pq = [(-count, char)for char, count in Counter(s).items()]
        heapify(pq)

        while pq:
            countFirst, charFirst = heappop(pq)
            if not ans or charFirst != ans[-1]:
                ans.append(charFirst)
                if countFirst + 1 != 0:
                    heappush(pq, (countFirst + 1, charFirst))
            else:
                if not pq:
                    return ''
                countSecond, charSecond = heappop(pq)
                ans.append(charSecond)
                if countSecond + 1 != 0:
                    heappush(pq, (countSecond + 1, charSecond))
                heappush(pq, (countFirst, charFirst))
        return "".join(ans)


s = "aab"
print(Solution().reorganizeString(s))
