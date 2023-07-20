class Solution:
    def insert(self, ins: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        N = len(ins)
        i = 0
        res = []
        # add non-overlapping intervals before new_interval to res
        while i < N and ins[i][1] < new_interval[0]:
            res.append(ins[i])
            i += 1

        # merge overlapping intervals with new_interval
        res.append(new_interval)
        while i < N and min(res[-1][1], ins[i][1]) >= max(ins[i][0], res[-1][0]):
            res[-1] = min(res[-1][0], ins[i][0]), max(res[-1][1], ins[i][1])
            i += 1

        # add rest of the non-overlapping intervals to res
        while i < N:
            res.append(ins[i])
            i += 1
        
        return res