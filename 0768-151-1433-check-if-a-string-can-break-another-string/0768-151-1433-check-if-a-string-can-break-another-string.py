# time complexity: O(nlogn)
# space complexity: O(n)
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        if s1 > s2:
            s1, s2 = s2, s1
        for i in range(len(s1)):
            if s1[i] > s2[i]:
                return False
        return True


# s1 = "abc"
# s2 = "xya"
# print(Solution().checkIfCanBreak(s1, s2))
# s1 = "abe"
# s2 = "acd"
# print(Solution().checkIfCanBreak(s1, s2))
# s1 = "leetcodee"
# s2 = "interview"
# print(Solution().checkIfCanBreak(s1, s2))
# s1 = "szy"
# s2 = "cid"
# print(Solution().checkIfCanBreak(s1, s2))
s1 = "bxfowqvnrhuzwqohquamvszkvunb"
s2 = "xjegbjccjjxfnsiearbsgsofywtq"
print(Solution().checkIfCanBreak(s1, s2))
