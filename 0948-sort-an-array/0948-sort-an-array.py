# time complexity: O(nlogn)
# space complexity: O(n)
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.mergeSortedArray(left, right)

    def mergeSortedArray(self, aList: List[int], bList: List[int]):
        sortedArray = []
        left = 0
        right = 0
        while left < len(aList) and right < len(bList):
            if aList[left] < bList[right]:
                sortedArray.append(aList[left])
                left += 1
            else:
                sortedArray.append(bList[right])
                right += 1
        sortedArray += aList[left:]
        sortedArray += bList[right:]
        return sortedArray

# time complexity: O(nlogn)
# space complexity: O(logn)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(n: int, i: int):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and nums[left] > nums[largest]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right
            if largest != i:
                nums[i], nums[largest] =  nums[largest], nums[i]
                heapify(n, largest)

        def heapSort():
            n = len(nums)
            for i in range(n // 2 - 1, -1, -1):
                heapify(n, i)
            for i in range(n - 1, -1, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify(i, 0)

        heapSort()
        return nums




# time complexity: O(d*(n + b)) 
# space complexity: O(n + b)
# n is the number of elements in the nums array
# d is the maximum number of digits 
# b is the size of the bucket used
class Solution:
    def radixSort(self, nums: List[int]) -> List[int]:
        maxVal = nums[0]
        for val in nums:
            maxVal = max(abs(val), maxVal)

        maxDigit = 0
        while maxVal > 0:
            maxDigit += 1
            maxVal = maxVal // 10

        placeVal = 1
        
        def bucketSort():
            buckets = [[] for _ in range(10)]
            for val in nums:
                digit = abs(val) / placeVal
                digit = int(digit % 10)
                buckets[digit].append(val)

            index = 0
            for digit in range(10):
                for val in buckets[digit]:
                    nums[index] = val
                    index += 1

        for _ in range(maxDigit):
            bucketSort()
            placeVal *= 10

        positives = [val for val in nums if val >= 0]
        negatives = [val for val in nums if val < 0]
        negatives.reverse()

        return negatives + positives
            
    def sortArray(self, nums: List[int]) -> List[int]:  
        return self.radixSort(nums)                                                      

# time complexity: O(n + k) k is element's range
# space complexity: O(n)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def countingSort():
            counts = {}
            minVal, maxVal = min(nums), max(nums)
            for val in nums:
                counts[val] = counts.get(val, 0) + 1

            index = 0
            for val in range(minVal, maxVal + 1, 1):
                while counts.get(val, 0) > 0:
                    nums[index] = val
                    index += 1
                    counts[val] -= 1

        countingSort()
        return nums
        
nums = [5, 2, 3, 1]
print(Solution().sortArray(nums))
nums = [5, 1, 1, 2, 0, 0]
print(Solution().sortArray(nums))
