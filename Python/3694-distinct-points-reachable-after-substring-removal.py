# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)

        move = {
            "U": (0, 1),
            "D": (0, -1),
            "L": (-1, 0),
            "R": (1, 0)
        }

        prefix = [(0, 0) for _ in range(n + 1)]
        x, y = 0, 0
        for i in range(n):
            dx, dy = move[s[i]]
            x, y = x + dx, y + dy
            prefix[i + 1] = (x, y)

        totalX, totalY = prefix[n]

        seen = set()

        for i in range(n - k + 1):
            px, py = prefix[i]
            qx, qy = prefix[i + k]
            finalX = px + (totalX - qx)
            finalY = py + (totalY - qy)
            seen.add((finalX, finalY))

        return len(seen)


s = "LUL"
k = 1
print(Solution().distinctPoints(s, k))
s = "UDLR"
k = 4
print(Solution().distinctPoints(s, k))
s = "UU"
k = 1
print(Solution().distinctPoints(s, k))
