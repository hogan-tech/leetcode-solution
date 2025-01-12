# time complexity: O(n)
# space complexity: O(n)
class TwoSum:

    def __init__(self):
        self.nums = {}

    def add(self, number: int) -> None:
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    def find(self, value: int) -> bool:
        for num in self.nums:
            remain = value - num
            if remain in self.nums:
                if remain != num or self.nums[num] > 1:
                    return True
        return False


twoSum = TwoSum()
twoSum.add(1)
twoSum.add(-1)
print(twoSum.find(0))
print(twoSum.find(7))
