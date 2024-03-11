# time complexity: O(nlogn)
# space complexity: O(n)
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        charIdx = {char: index for index, char in enumerate(order)}

        def customSort(char):
            return charIdx.get(char, float('inf'))
        sortedString = sorted(s, key=customSort)
        return "".join(sortedString)


order = "cba"
s = "abcd"
print(Solution().customSortString(order, s))
