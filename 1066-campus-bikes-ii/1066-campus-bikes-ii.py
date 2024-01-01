from functools import lru_cache
from typing import List

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(workers, bikes):
            if not workers or not bikes:
                return 0
            first_worker = workers[0]
            other_workers = workers[1:]
            out = float('inf')
            for idx,bike in enumerate(bikes):
                dist = abs(first_worker[0]-bike[0]) + abs(first_worker[1]- bike[1])
                other_bikes = bikes[:idx] + bikes[idx+1:]
                out = min(out, dist + dfs(other_workers, other_bikes))
            return out

        workers = tuple(tuple(w) for w in workers)
        bikes = tuple(tuple(b) for b in bikes)

        return dfs(workers, bikes)            


workers = [[0, 0], [2, 1]]
bikes = [[1, 2], [3, 3]]
print(Solution().assignBikes(workers, bikes))
