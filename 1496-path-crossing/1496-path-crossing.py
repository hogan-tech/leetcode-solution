# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        moves = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0)
        }

        visited = {(0, 0)}
        x = 0
        y = 0
        for c in path:
            dx = moves[c][0]
            dy = moves[c][1]
            x += dx
            y += dy
            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))
        return False


path = "NESW"
print(Solution().isPathCrossing(path))
