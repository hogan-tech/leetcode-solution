# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removeAndScore(s, first, second, points_value):
            stack = []
            points = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    points += points_value
                else:
                    stack.append(char)
            remaining = ''.join(stack)
            return remaining, points

        if x >= y:
            s, points = removeAndScore(s, 'a', 'b', x)
            s, additional_points = removeAndScore(s, 'b', 'a', y)
            points += additional_points
        else:
            s, points = removeAndScore(s, 'b', 'a', y)
            s, additional_points = removeAndScore(s, 'a', 'b', x)
            points += additional_points

        return points


s = "aabbaaxybbaabb"
x = 5
y = 4
print(Solution().maximumGain(s, x, y))
