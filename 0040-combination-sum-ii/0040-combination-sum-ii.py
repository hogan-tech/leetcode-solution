class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(start: int, remain: int, comb: List[int]):
            if remain == 0:
                result.append(list(comb))
                return
            if remain < 0:
                return 
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                backtrack(i + 1, remain - candidates[i], comb)
                comb.pop()
                
        backtrack(0, target, [])
        return result
        