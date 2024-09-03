# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result = ""
        for digitChar in s:
            result += str(ord(digitChar) - ord('a') + 1)
        while k > 0:
            temp = 0
            for digit in result:
                temp += int(digit)
            result = str(temp)
            k -= 1

        return int(result)


s = "iaozzbyqzwbpurzze"
k = 2
print(Solution().getLucky(s, k))
