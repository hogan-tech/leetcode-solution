# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.discount = discount
        self.productPriceMap = defaultdict(int)
        self.customerId = 0
        self.n = n
        for product, price in zip(products, prices):
            self.productPriceMap[product] = price

    def getBill(self, product: List[int], amount: List[int]) -> float:
        result = 0
        self.customerId += 1
        for i in range(len(product)):
            currProduct = product[i]
            currAmount = amount[i]
            currPrice = self.productPriceMap[currProduct]
            bill = currAmount * currPrice
            pay = bill * (((100 - self.discount) / 100)
                          if self.customerId % self.n == 0 else 1)
            result += pay
        return result


'''
n = 3
discount = 50
products = [1, 2, 3, 4, 5, 6, 7]
prices = [100, 200, 300, 400, 300, 200, 100]
subtotal = amount[j] * prices[j] = bill
pay = bill * ((100 - discount) / 100) = amount[j] * prices[j] * ((100 - discount) / 100)


getBill
product, amount
[1, 2], [1, 2]


Cashier cashier = new Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]);
cashier.getBill([1,2],[1,2]);                        // return 500.0. 1st customer, no discount.
                                                     // bill = 1 * 100 + 2 * 200 = 500.

cashier.getBill([3,7],[10,10]);                      // return 4000.0. 2nd customer, no discount.
                                                     // bill = 10 * 300 + 10 * 100 = 4000.

cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]);    // return 800.0. 3rd customer, 50% discount.
                                                     // Original bill = 1600
                                                     // Actual bill = 1600 * ((100 - 50) / 100) = 800.

cashier.getBill([4],[10]);                           // return 4000.0. 4th customer, no discount.

cashier.getBill([7,3],[10,10]);                      // return 4000.0. 5th customer, no discount.

cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]); // return 7350.0. 6th customer, 50% discount.
                                                     // Original bill = 14700, but with
                                                     // Actual bill = 14700 * ((100 - 50) / 100) = 7350.

cashier.getBill([2,3,5],[5,3,2]);                    // return 2500.0.  7th customer, no discount.

'''

cashier = Cashier(3, 50, [1, 2, 3, 4, 5, 6, 7], [
                  100, 200, 300, 400, 300, 200, 100])
print(cashier.getBill([1, 2], [1, 2]))
print(cashier.getBill([3, 7], [10, 10]))
print(cashier.getBill([1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1]))
print(cashier.getBill([4], [10]))
print(cashier.getBill([7, 3], [10, 10]))
print(cashier.getBill([7, 5, 3, 1, 6, 4, 2], [10, 10, 10, 9, 9, 9, 7]))
print(cashier.getBill([2, 3, 5], [5, 3, 2]))
