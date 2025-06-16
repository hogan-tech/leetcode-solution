# time complexity: O(n)
# space complexity: O(n)
import re


class Solution:
    def generateTag(self, caption: str) -> str:
        caption = re.sub(r'[^a-zA-Z ]', '', caption)
        words = caption.split()
        if not words:
            return "#"
        tag = words[0].lower()
        for word in words[1:]:
            tag += word.capitalize()
        return ('#' + tag)[:100]


caption = "Leetcode daily streak achieved"
print(Solution().generateTag(caption))
caption = "can I Go There"
print(Solution().generateTag(caption))
caption = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
print(Solution().generateTag(caption))
