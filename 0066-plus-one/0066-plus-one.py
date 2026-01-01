class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numStr = ''.join([str(digit) for digit in digits])
        numStr = str(int(numStr) + 1)
        return [int(digit) for digit in numStr]
        
        