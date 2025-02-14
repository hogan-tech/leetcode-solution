# time complexity: O(1)
# space complexity: O(n)
class ProductOfNumbers:

    def __init__(self):
        self.prefixProduct = [1]
        self.zeroIdx = float('inf')
        self.n = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.zeroIdx = self.n
            num = 1
        if self.prefixProduct:
            self.prefixProduct.append(self.prefixProduct[-1] * num)
        else:
            self.prefixProduct.append(num)
        self.n += 1

    def getProduct(self, k: int) -> int:
        if self.zeroIdx != float('inf') and self.n - k <= self.zeroIdx:
            return 0
        return self.prefixProduct[-1] // self.prefixProduct[-k - 1]


productOfNumbers = ProductOfNumbers()
productOfNumbers.add(0)
productOfNumbers.add(5)
productOfNumbers.add(6)
print(productOfNumbers.getProduct(2))
print(productOfNumbers.getProduct(2))
productOfNumbers.add(8)
print(productOfNumbers.getProduct(4))
productOfNumbers.add(2)
# productOfNumbers = ProductOfNumbers()
# productOfNumbers.add(3)
# productOfNumbers.add(0)
# productOfNumbers.add(2)
# productOfNumbers.add(5)
# productOfNumbers.add(4)
# print(productOfNumbers.getProduct(2))
# print(productOfNumbers.getProduct(3))
# print(productOfNumbers.getProduct(4))
# productOfNumbers.add(8)
# print(productOfNumbers.getProduct(2))
