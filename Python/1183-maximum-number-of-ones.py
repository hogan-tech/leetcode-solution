# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        count = []
        for r in range(sideLength):
            for c in range(sideLength):
                num = (1+(width - c - 1) // sideLength) * \
                    (1+(height-r-1)//sideLength)
                count.append(num)
        count.sort(reverse=True)
        return sum(count[:maxOnes])


width = 3
height = 3
sideLength = 2
maxOnes = 1
print(Solution().maximumNumberOfOnes(width, height, sideLength, maxOnes))
width = 3
height = 3
sideLength = 2
maxOnes = 2
print(Solution().maximumNumberOfOnes(width, height, sideLength, maxOnes))
