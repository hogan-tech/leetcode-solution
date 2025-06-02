from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        totalSeats = [0 for _ in range(n + 2)]
        for first, last, seat in bookings:
            totalSeats[first] += seat
            totalSeats[last + 1] -= seat
        for i in range(1, n + 1):
            totalSeats[i] += totalSeats[i - 1]
        return totalSeats[1:-1]

'''
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10   0  -10
Booking 2 reserved:      20   0  -20
Booking 3 reserved:      25   0   0  25
Total seats:         10  55  45  25  25
Hence, answer = [10,55,45,25,25]

[1, 2, 10]


'''
bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
n = 5
print(Solution().corpFlightBookings(bookings, n))
bookings = [[1, 2, 10], [2, 2, 15]]
n = 2
print(Solution().corpFlightBookings(bookings, n))
