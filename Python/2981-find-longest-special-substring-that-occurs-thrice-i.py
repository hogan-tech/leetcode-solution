# time complexity: O(n^2)
# space complexity: O(n^2)
class Solution:
    def maximumLength(self, s: str) -> int:
        count = {}
        for start in range(len(s)):
            character = s[start]
            subString = 0
            for end in range(start, len(s)):
                if character == s[end]:
                    subString += 1
                    count[(character, subString)] = (
                        count.get((character, subString), 0) + 1)
                else:
                    break
        result = 0
        for item in count.items():
            length = item[0][1]
            if item[1] >= 3 and length > result:
                result = length
        if result == 0:
            return -1
        return result
    

s = "aaaa"
print(Solution().maximumLength(s))
s = "abcdef"
print(Solution().maximumLength(s))
s = "abcaba"
print(Solution().maximumLength(s))
