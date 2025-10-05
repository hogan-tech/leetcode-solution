class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW = len(heights)
        COL = len(heights[0])

        pVisited = set()
        oVisited = set()

        pQueue = deque()
        oQueue = deque()

        for r in range(ROW):
            pQueue.append((r, 0))
            oQueue.append((r, COL - 1))

        for c in range(COL):
            pQueue.append((0, c))
            oQueue.append((ROW - 1, c))

        def bfs(queue):
            visited = set()
            while queue:
                currR, currC = queue.popleft()
                visited.add((currR, currC))
                for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nextR = currR + dR
                    nextC = currC + dC
                    if 0 <= nextR < ROW and 0 <= nextC < COL and (nextR, nextC) not in visited and heights[nextR][nextC] >= heights[currR][currC]:
                        queue.append((nextR, nextC))
            
            return visited

        pVisited = bfs(pQueue)
        oVisited = bfs(oQueue)

        return list(pVisited.intersection(oVisited))


'''
00 01 02 03 04 05
10
20
30
40
50

'''