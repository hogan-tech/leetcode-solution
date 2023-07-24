from queue import Queue
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row = len(mat)
        if row == 0:
            return mat
        col = len(mat[0])
        dist = [[float('inf') for _ in range(col)] for _ in range(row)]
        q = Queue()

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.put((i, j))

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while not q.empty():
            curr = q.get()
            for i in range(4):
                new_r = curr[0] + dir[i][0]
                new_c = curr[1] + dir[i][1]
                if 0 <= new_r < row and 0 <= new_c < col:
                    if dist[new_r][new_c] > dist[curr[0]][curr[1]] + 1:
                        dist[new_r][new_c] = dist[curr[0]][curr[1]] + 1
                        q.put((new_r, new_c))
        return dist