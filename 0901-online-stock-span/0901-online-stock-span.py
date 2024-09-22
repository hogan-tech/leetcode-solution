# time complexity: O(1)
# space complexity: O(n)
class StockSpanner:

    def __init__(self):
        self.stockPrice = []

    def next(self, price: int) -> int:
        count = 1
        print(self.stockPrice)
        while self.stockPrice and self.stockPrice[-1][0] <= price:
            count += self.stockPrice.pop()[1]
        self.stockPrice.append([price, count])

        return count


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
print(obj.next(100))
print(obj.next(80))
print(obj.next(60))
print(obj.next(70))
print(obj.next(60))
print(obj.next(75))
print(obj.next(85))
