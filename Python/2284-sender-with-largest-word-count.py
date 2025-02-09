# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        senderDict = defaultdict(int)
        for i, sender in enumerate(senders):
            wordCount = len(messages[i].split(" "))
            senderDict[sender] += wordCount

        maxWordCount = max(senderDict.values())
        result = ""
        for sender, wordCount in senderDict.items():
            if wordCount == maxWordCount:
                result = max(result, sender)
        return result


messages = ["Hello userTwooo", "Hi userThree",
            "Wonderful day Alice", "Nice day userThree"]
senders = ["Alice", "userTwo", "userThree", "Alice"]
print(Solution().largestWordCount(messages, senders))
messages = ["How is leetcode for everyone", "Leetcode is useful for practice"]
senders = ["Bob", "Charlie"]
print(Solution().largestWordCount(messages, senders))
