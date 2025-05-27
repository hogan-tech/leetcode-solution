# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        countFirst = countSecond = countPattern = 0
        for c in text:
            if c == pattern[1]:
                countSecond += 1
                countPattern += countFirst
            if c == pattern[0]:
                countFirst += 1

        return countPattern + max(countSecond, countFirst)


'''
acc
ac
[a,c,c]
[a,a,c,c]
     |
      
[a,c,c,c]
 |
aacc -> 4
accc -> 3

[a,c,a,c,c,c] -> 4 + 3 = 7
[a,a,c,a,c,c,c] -> 4 + 4 + 3 = 11
[a,c,a,c,c,c,c] -> 5 + 4 = 9
ac



aabb
ab

aaabb -> 6
aabbb -> 6

'''
text = "abdcdbc"
pattern = "ac"
print(Solution().maximumSubsequenceCount(text, pattern))
text = "aabb"
pattern = "ab"
print(Solution().maximumSubsequenceCount(text, pattern))
