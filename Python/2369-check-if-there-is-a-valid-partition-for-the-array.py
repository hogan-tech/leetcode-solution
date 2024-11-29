class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        queue = deque([0])
        seen = set()
        while queue:
            i = queue.popleft()
            if i == N:
                return True
            if i + 1 < N and nums[i] == nums[i + 1] and i + 2 not in seen:
                seen.add(i + 2)
                queue.append(i + 2)
            if i + 2 < N and (nums[i] == nums[i + 1] == nums[i + 2] or nums[i] + 2 == nums[i + 1] + 1 == nums[i + 2]) and i + 3 not in seen:
                seen.add(i + 3)
                queue.append(i + 3)
        return False