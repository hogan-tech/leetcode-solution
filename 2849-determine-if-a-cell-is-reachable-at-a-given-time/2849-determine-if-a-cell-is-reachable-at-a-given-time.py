#time complexity: O(1)
#space complexity: O(1)

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        width, height = abs(fx-sx), abs(fy-sy)
        if width == 0 and height == 0 and t == 1:
            return False
        return t >= max(height, width)


sx = 2
sy = 4
fx = 7
fy = 7
t = 6


print(Solution().isReachableAtTime(sx, sy, fx, fy, t))
