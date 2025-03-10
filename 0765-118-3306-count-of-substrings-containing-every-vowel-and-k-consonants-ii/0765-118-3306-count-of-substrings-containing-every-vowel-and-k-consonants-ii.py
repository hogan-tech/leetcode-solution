# time complexity: O(n)
# space compelxity: O(n)
from typing import Counter


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowelCounter = Counter()

        left = 0
        right = 0
        consonant = 0
        result = 0
        nextConsonant = [0] * len(word)
        nextConsonantIndex = len(word)

        for i in range(len(word) - 1, -1, -1):
            nextConsonant[i] = nextConsonantIndex
            if word[i] not in vowels:
                nextConsonantIndex = i

        while right < len(word):
            currC = word[right]
            if currC in vowels:
                vowelCounter[currC] += 1
            else:
                consonant += 1

            while consonant > k:
                removeC = word[left]
                if removeC in vowels:
                    vowelCounter[removeC] -= 1
                    if vowelCounter[removeC] == 0:
                        del vowelCounter[removeC]
                else:
                    consonant -= 1
                left += 1

            while left < len(word) and len(vowelCounter) == 5 and consonant == k:
                result += nextConsonant[right] - right
                removeC = word[left]
                if removeC in vowels:
                    vowelCounter[removeC] -= 1
                    if vowelCounter[removeC] == 0:
                        del vowelCounter[removeC]
                else:
                    consonant -= 1
                left += 1

            right += 1

        return result


'''
a a d i e u o h
l
            r
'''
word = "aadieuoh"
k = 1
print(Solution().countOfSubstrings(word, k))

# word = "iqeaouqi"
# k = 2
# print(Solution().countOfSubstrings(word, k))
# word = "aeiouqqieaouqq"
# k = 1
# print(Solution().countOfSubstrings(word, k))
# word = "aeioqq"
# k = 1
# print(Solution().countOfSubstrings(word, k))
# word = "aeiou"
# k = 0
# print(Solution().countOfSubstrings(word, k))
