class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        left = 0
        while left < n:
            right = left
            if right + 1 < n and arr[right] < arr[right + 1]:
                while right + 1 < n and arr[right] < arr[right + 1]:
                    right += 1
                if right + 1 < n and arr[right] > arr[right + 1]:
                    while right + 1 < n and arr[right] > arr[right + 1]:
                        right += 1
                    result = max(result, right - left + 1)
            left = max(right, let + 1)
        return result
