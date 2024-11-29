# time complexity: O(n^2)
# space complexity: O(1)
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        for _ in range(9):
            for c in word:
                temp = chr(ord(c) + 1)
                word += temp
        return word[k - 1]

# word = a
# k = 1, k = 2
# gene b -> word ab
# k = 3, k = 4
# gene bc -> word abbc
# k = 5 -> k = 8
# gene bccd -> word abbcbccd
# k = 9 -> k = 16
# gene bccdcdde -> word abbcbccdbccdcdde


k = 10
print(Solution().kthCharacter(k))
