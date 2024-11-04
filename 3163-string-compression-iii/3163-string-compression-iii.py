class Solution:
    def compressedString(self, word: str) -> str:
        result = ""
        prevC = ""
        for i in range(len(word)):
            currC = word[i]
            if prevC == currC:
                if count == 9:
                    count = 1
                    result += str(count) + word[i]
                else:
                    count += 1
                    result = result[:-2] + str(count) + word[i]
            else:
                count = 1
                result += str(count) + word[i]
            prevC = word[i]

        return result


word = "aaaaaaaaaabcde"
print(Solution().compressedString(word))
word = "aaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaabb"
print(Solution().compressedString(word))
