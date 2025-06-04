# time complexity: O(n^2)
# space complexity: O(n)
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        targetLen = len(word) - numFriends + 1
        result = ""
        for i in range(len(word)):
            result = max(result, (word[i:i + targetLen]))
        return result


'''
string length from 1 -> len(word) - n + 1
find len(word) - n + 1 largest string

xxxxxxxxx = 10
n = 5
0 1 2 3 4
xxxxxx x x x x
x xxxxxx x x x 
x x xxxxxx x x
x x x xxxxxx x
x x x x xxxxxx

dbca
1  2
dbc a
d bca

gggg

1 2 3 4
g g g g
'''
word = "dbca"
numFriends = 2
print(Solution().answerString(word, numFriends))
word = "gggg"
numFriends = 4
print(Solution().answerString(word, numFriends))
