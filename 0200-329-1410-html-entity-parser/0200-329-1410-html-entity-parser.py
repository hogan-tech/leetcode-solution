# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def entityParser(self, text: str) -> str:
        specialCharMap = {
            "&quot;": "\"@@@@",
            "&apos;": "\'@@@@",
            "&amp;": "&@@@@",
            "&gt;": ">@@@@",
            "&lt;": "<@@@@",
            "&frasl;": "/@@@@",
        }

        for word in specialCharMap:
            if word in text:
                text = text.replace(word, specialCharMap[word])

        return text.replace("@@@@", "")


text = "&amp; is an HTML entity but &ambassador; is not."
print(Solution().entityParser(text))
text = "and I quote: &quot;...&quot;"
print(Solution().entityParser(text))
text = "&amp;quot;&amp;apos;&amp;amp;&amp;gt;&amp;lt;&amp;frasl;"
print(Solution().entityParser(text))
