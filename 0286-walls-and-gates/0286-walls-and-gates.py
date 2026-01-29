class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        INF = 2147483647
        ROW = len(rooms)
        COL = len(rooms[0])
        queue = deque()
        for r in range(ROW):
            for c in range(COL):
                if rooms[r][c] == 0:
                    queue.append((1, r, c))
        
        while queue:
            currDistance, currR, currC = queue.popleft()

            for dR, dC in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nextR = currR + dR
                nextC = currC + dC
                if 0 <= nextR < ROW and 0 <= nextC < COL and rooms[nextR][nextC] == INF:
                    rooms[nextR][nextC] = currDistance
                    queue.append((currDistance + 1, nextR, nextC))
        
        return rooms
        