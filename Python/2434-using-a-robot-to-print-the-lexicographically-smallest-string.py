# time complexity: O(n)
# space complexity: O(n)
from typing import Counter


class Solution:
    def robotWithString(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        result = []
        minCharacter = "a"
        for c in s:
            stack.append(c)
            counter[c] -= 1
            while minCharacter != "z" and counter[minCharacter] == 0:
                minCharacter = chr(ord(minCharacter) + 1)
            while stack and stack[-1] <= minCharacter:
                result.append(stack.pop())
        return "".join(result)


'''
p: a
s: 
t: bdd

'''
s = "zza"
print(Solution().robotWithString(s))
s = "bac"
print(Solution().robotWithString(s))
s = "bdda"
print(Solution().robotWithString(s))
