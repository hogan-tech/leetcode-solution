class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monoQueue = deque()
        result = []

        left = 0
        right = 0
        while right < len(nums):
            while monoQueue and nums[monoQueue[-1]] < nums[right]:
                monoQueue.pop()
            monoQueue.append(right)
        
            if left > monoQueue[0]:
                monoQueue.popleft()
            
            if (right + 1) >= k:
                result.append(nums[monoQueue[0]])
                left += 1
            right += 1
        
        return result