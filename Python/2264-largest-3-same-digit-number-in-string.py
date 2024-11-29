# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def largestGoodInteger(self, num):
        arr = ["999", "888", "777", "666", "555",
               "444", "333", "222", "111", "000"]
        for s in arr:
            if s in num:
                return s
        return ""


num = "6777133339"
print(Solution().largestGoodInteger(num))
