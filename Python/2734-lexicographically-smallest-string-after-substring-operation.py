# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def smallestString(self, s: str) -> str:
        result = ""
        flag = False
        for i in range(len(s)):
            if s[i] == 'a' and flag:
                result += s[i:]
                break
            if s[i] == 'a':
                result += s[i]
            else:
                result += chr(ord(s[i]) - 1)
                flag = True
        if flag == False:
            result = s[:len(s) - 1] + "z"

        return result


'''
test case 1:
x x a x x x
l r
0 1
test case 5
x x a a x x
l r  
0 2
test case 2:
a x x x x
  l     r
1 4
test case 3:
a a a x x x x
      l     r
3 6
test case 
a a 
  l
  r
1 1
test case 
a
l
r 
0 0
'''

s = "cbabc"
print(Solution().smallestString(s))
s = "aa"
print(Solution().smallestString(s))
s = "acbbc"
print(Solution().smallestString(s))
