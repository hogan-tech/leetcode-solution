# time complexity: O(n)
# space complexity: O(n)
from typing import Counter


class Solution:
    def largestPalindromic(self, num: str) -> str:
        freq = Counter(num)
        firstHalf = []
        middle = ""

        for digit in range(9, -1, -1):
            digitChar = str(digit)

            if digitChar in freq:
                digitCount = freq[digitChar]

                numPairs = digitCount // 2

                if numPairs:
                    if not firstHalf and not digit:
                        freq['0'] = 1
                    else:
                        firstHalf.append(digitChar * numPairs)
                if digitCount % 2 and not middle:
                    middle = digitChar
        if not middle and not firstHalf:
            return "0"

        return "".join(firstHalf + [middle] + firstHalf[::-1])


num = "444947137"
print(Solution().largestPalindromic(num))
num = "00009"
print(Solution().largestPalindromic(num))
num = "00001105"
print(Solution().largestPalindromic(num))
num = "00011"
print(Solution().largestPalindromic(num))
