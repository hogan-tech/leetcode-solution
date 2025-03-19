# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        result = 0
        skip = False

        for i in range(1, len(word)):
            prev = ord(word[i-1])
            curr = ord(word[i])
            diff = curr - prev

            if not skip and -1 <= diff <= 1:
                result += 1
                skip = True
            else:
                skip = False

        return result


'''
1 -> 1
2 -> 2
3 -> 1 & 3
4 -> 1 & 3
aaa
 aaa
  aaa
'''
word = "aaaa"
print(Solution().removeAlmostEqualCharacters(word))
'''
3 -> 1 & 3
abd
 bdd
  dez
'''
word = "abddez"
# print(Solution().removeAlmostEqualCharacters(word))
'''
5 -> 2 & 4
6 -> 1 & 3 & 5
7 -> 2 & 4 & 6
8 -> 1 & 3 & 5 & 7
zyx
 yxy
  xyx
   yxy
    xyz
'''
word = "zyxyxyz"
# print(Solution().removeAlmostEqualCharacters(word))
