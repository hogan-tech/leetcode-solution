# time complexity: O((m+n)logn)
# m means maximum calls reserve() or unreserve()
# space complexity: O(n)
import heapq


class SeatManager:

    def __init__(self, n: int):
        self.availableSeats = [i for i in range(1, n+1)]

    def reserve(self) -> int:
        seatNumber = heapq.heappop(self.availableSeats)
        return seatNumber

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.availableSeats, seatNumber)
        return


# Your SeatManager object will be instantiated and called as such:
obj = SeatManager(5)
print(obj.reserve())
print(obj.reserve())
obj.unreserve(2)
print(obj.reserve())
print(obj.reserve())
print(obj.reserve())
print(obj.reserve())
obj.unreserve(5)
