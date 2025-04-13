# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        xDis = abs(z - x)
        yDis = abs(z - y)
        if xDis == yDis:
            return 0
        if xDis > yDis:
            return 2
        else:
            return 1


x = 2
y = 7
z = 4
print(Solution().findClosest(x, y, z))
x = 2
y = 5
z = 6
print(Solution().findClosest(x, y, z))
x = 1
y = 5
z = 3
print(Solution().findClosest(x, y, z))
