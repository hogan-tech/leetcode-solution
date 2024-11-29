# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        count = 0
        keyMap = {}
        prevIdx = 0
        for i in range(len(keyboard)):
            keyMap[keyboard[i]] = i
        for i in range(len(word)):
            count += abs(keyMap[word[i]] - prevIdx)
            prevIdx = keyMap[word[i]]
        return count


keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"

print(Solution().calculateTime(keyboard, word))
