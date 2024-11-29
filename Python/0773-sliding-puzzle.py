# time complexity: O((m*n)! * (mn)^2)
# space complexity: O((m*n)!)
from typing import List


class Solution:

    directions = [
        [1, 3],
        [0, 2, 4],
        [1, 5],
        [0, 4],
        [3, 5, 1],
        [4, 2],
    ]

    def slidingPuzzle(self, board: List[List[int]]) -> int:

        def swap(s, i, j):
            s = list(s)
            s[i], s[j] = s[j], s[i]
            return "".join(s)

        startState = "".join(str(num) for row in board for num in row)

        visited = {}

        def dfs(state, zero_pos, moves):

            if state in visited and visited[state] <= moves:
                return
            visited[state] = moves

            for nextPos in self.directions[zero_pos]:
                newState = swap(
                    state, zero_pos, nextPos
                )
                dfs(newState, nextPos, moves + 1)

        dfs(startState, startState.index("0"), 0)

        return visited.get("123450", -1)


board = [[1, 2, 3], [4, 0, 5]]
print(Solution().slidingPuzzle(board))
board = [[1, 2, 3], [5, 4, 0]]
print(Solution().slidingPuzzle(board))
board = [[4, 1, 2], [5, 0, 3]]
print(Solution().slidingPuzzle(board))
