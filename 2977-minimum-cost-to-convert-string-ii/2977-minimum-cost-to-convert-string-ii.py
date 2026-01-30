# time complexity: O(n^2 + m^3 + mL)
# space complexity: O(n^2)
from typing import List

INF = 10**18
INF_INT = 10**9

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)
        m = len(original)

        child = [[-1] * 26]
        tid = [-1]

        def new_node() -> int:
            child.append([-1] * 26)
            tid.append(-1)
            return len(child) - 1

        idx = -1

        def add(word: str) -> int:
            nonlocal idx
            node = 0
            for ch in word:
                c = ord(ch) - 97
                nxt = child[node][c]
                if nxt == -1:
                    nxt = new_node()
                    child[node][c] = nxt
                node = nxt
            if tid[node] == -1:
                idx += 1
                tid[node] = idx
            return tid[node]

        edges = []
        for i in range(m):
            x = add(original[i])
            y = add(changed[i])
            edges.append((x, y, cost[i]))

        P = idx + 1
        if P == 0:
            return 0 if source == target else -1

        dist = [[INF_INT] * P for _ in range(P)]
        for i in range(P):
            dist[i][i] = 0
        for x, y, w in edges:
            if w < dist[x][y]:
                dist[x][y] = w

        for k in range(P):
            dk = dist[k]
            for i in range(P):
                di = dist[i]
                dik = di[k]
                if dik == INF_INT:
                    continue
                base = dik
                for j in range(P):
                    nd = base + dk[j]
                    if nd < di[j]:
                        di[j] = nd

        dp = [INF] * (n + 1)
        dp[0] = 0

        sArr = [ord(c) - 97 for c in source]
        tArr = [ord(c) - 97 for c in target]

        for j in range(n):
            if dp[j] >= INF:
                continue
            base = dp[j]
            if source[j] == target[j] and base < dp[j + 1]:
                dp[j + 1] = base

            u = 0
            v = 0
            for i in range(j, n):
                u = child[u][sArr[i]]
                v = child[v][tArr[i]]
                if u == -1 or v == -1:
                    break
                uid = tid[u]
                vid = tid[v]
                if uid != -1 and vid != -1:
                    w = dist[uid][vid]
                    if w != INF_INT:
                        ni = i + 1
                        cand = base + w
                        if cand < dp[ni]:
                            dp[ni] = cand

        result = dp[n]
        return -1 if result >= INF else result


source = "abcd"
target = "acbe"
original = ["a", "b", "c", "c", "e", "d"]
changed = ["b", "c", "b", "e", "b", "e"]
cost = [2, 5, 5, 1, 2, 20]
print(Solution().minimumCost(source, target, original, changed, cost))
source = "abcdefgh"
target = "acdeeghh"
original = ["bcd", "fgh", "thh"]
changed = ["cde", "thh", "ghh"]
cost = [1, 3, 5]
print(Solution().minimumCost(source, target, original, changed, cost))
source = "abcdefgh"
target = "addddddd"
original = ["bcd", "defgh"]
changed = ["ddd", "ddddd"]
cost = [100, 1578]
print(Solution().minimumCost(source, target, original, changed, cost))
