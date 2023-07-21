class Solution:
    def insert(self, ins: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        N = len(ins)
        res = []
        i = 0

        while i < N and ins[i][1] < new_interval[0]:
            res.append(ins[i])
            i += 1

        res.append(new_interval)

        while i < N and min(res[-1][1], ins[i][1]) >= max(res[-1][0], ins[i][0]):
            res[-1] = min(res[-1][0], ins[i][0]), max(res[-1][1], ins[i][1])
            i += 1

        while i < N:
            res.append(ins[i])
            i += 1

        return res