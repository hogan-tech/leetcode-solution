# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        answer = 0
        prefixCount = [0] * 26

        for i in range(len(s)):
            prefixCount[ord(s[i]) - ord("a")] += 1
            answer += prefixCount[ord(s[i]) - ord("a")]
        return answer


s = "abacad"
print(Solution().numberOfSubstrings(s))
