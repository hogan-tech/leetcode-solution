from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        events.sort()
        xs = []
        prevY = events[0][0]
        total = 0
        areas = []

        def unionLen(intervals):
            intervals.sort()
            result = 0
            end = -10**30
            for a, b in intervals:
                if a > end:
                    result += b - a
                    end = b
                elif b > end:
                    result += b - end
                    end = b
            return result

        for y, typ, x1, x2 in events:
            if y > prevY and xs:
                h = y - prevY
                w = unionLen(xs)
                areas.append((prevY, h, w))
                total += h * w
            if typ == 1:
                xs.append((x1, x2))
            else:
                xs.remove((x1, x2))
            prevY = y

        half = total / 2
        acc = 0
        for y, h, w in areas:
            if acc + h * w >= half:
                return y + (half - acc) / w
            acc += h * w

        return 0.0


squares = [[0, 0, 1], [2, 2, 1]]
print(Solution().separateSquares(squares))
squares = [[0, 0, 2], [1, 1, 1]]
print(Solution().separateSquares(squares))
