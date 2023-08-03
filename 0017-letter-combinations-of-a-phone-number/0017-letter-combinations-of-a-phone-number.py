
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        numberMap = {}
        numberMap["2"] = set("abc")
        numberMap["3"] = set("def")
        numberMap["4"] = set("ghi")
        numberMap["5"] = set("jkl")
        numberMap["6"] = set("mon")
        numberMap["7"] = set("pqrs")
        numberMap["8"] = set("tuv")
        numberMap["9"] = set("wxyz")

        def backtrack(index: int, path: List):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            possible_letters = numberMap[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()


        combinations = []
        backtrack(0, [])

        return combinations