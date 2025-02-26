# time complexity: O(1)
# space complexity: O(1)
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        finalHour = hour + minutes / 60
        hourDegree = (finalHour * 360 / 12) % 360
        minuteDegree = (minutes * 360 / 60) % 360
        hourMinDegree = abs(hourDegree - minuteDegree)
        return min(hourMinDegree, 360 - hourMinDegree)


hour = 12
minutes = 30
print(Solution().angleClock(hour, minutes))
hour = 3
minutes = 30
print(Solution().angleClock(hour, minutes))
hour = 3
minutes = 15
print(Solution().angleClock(hour, minutes))
hour = 1
minutes = 57
print(Solution().angleClock(hour, minutes))
