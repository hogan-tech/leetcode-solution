# time complexity: O(n*n!)
# space complexity: O(n)
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        sCount = [0] * 26
        for c in s:
            sCount[ord(c) - ord('a')] += 1

        result = None
        def backtrack(i: int, prefix: str, count: list, greater: bool):
            nonlocal result
            if result is not None and prefix >= result:
                return
            if i == n:
                if prefix > target:
                    if result is None or prefix < result:
                        result = prefix
                return
            for c in range(26):
                if count[c] == 0:
                    continue
                currC = chr(c + ord('a'))
                if not greater and currC < target[i]:
                    continue
                if not greater and currC == target[i]:
                    count[c] -= 1
                    backtrack(i + 1, prefix + currC, count, False)
                    count[c] += 1
                elif greater or currC > target[i]:
                    count[c] -= 1
                    backtrack(i + 1, prefix + currC, count, True)
                    count[c] += 1

        backtrack(0, "", sCount, False)
        
        if result:
            return result
        
        return ""


s = "abc"
target = "bba"
print(Solution().lexGreaterPermutation(s, target))
s = "leet"
target = "code"
print(Solution().lexGreaterPermutation(s, target))
s = "baba"
target = "bbaa"
print(Solution().lexGreaterPermutation(s, target))
