# time complexity: O(n*k)
# space complexity: O(n*k)
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        visited = set()
        for i in range(k, len(s) + 1):
            temp = s[i - k: i]
            if temp not in visited:
                visited.add(temp)
                need -= 1
                if need == 0:
                    return True
        return False


s = "00110110"
k = 2
print(Solution().hasAllCodes(s, k))
s = "0110"
k = 1
print(Solution().hasAllCodes(s, k))
s = "0110"
k = 2
print(Solution().hasAllCodes(s, k))
