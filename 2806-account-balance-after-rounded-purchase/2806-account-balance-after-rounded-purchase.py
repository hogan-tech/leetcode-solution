class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        remainder = purchaseAmount % 10
        if remainder >= 5:
            purchaseAmount = ((purchaseAmount // 10) + 1) * 10
        else:
            purchaseAmount = (purchaseAmount // 10) * 10
        return 100 - purchaseAmount