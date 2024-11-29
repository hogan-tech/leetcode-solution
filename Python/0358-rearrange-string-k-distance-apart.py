import collections
import heapq


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1
        freqs = [[-d[k], k] for k in d]
        heapq.heapify(freqs)
        cooling = {}
        res = []
        while freqs:
            freq, c = heapq.heappop(freqs)
            res.append(c)
            freq += 1
            if freq < 0:
                cooling[c] = [freq, c]
            if len(res) >= k and res[-k] in cooling:
                prevFreq, prevC = cooling.pop(res[-k])
                heapq.heappush(freqs, [prevFreq, prevC])
        return ''.join(res) if len(res) == len(s) else ""
