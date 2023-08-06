class Solution:
    def finalString(self, s: str) -> str:
        temp = ""
        for i in range(len(s)):
            temp += s[i]
            if s[i] == "i":
                temp = temp.replace("i","")
                temp = temp[::-1]
        return temp