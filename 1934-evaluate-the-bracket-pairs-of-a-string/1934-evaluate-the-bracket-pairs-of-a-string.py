# time complexity: O(n)
# space complexity: O(n)
from collections import defaultdict
from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledgeMap = defaultdict(str)
        for key, value in knowledge:
            knowledgeMap[key] = value

        stack = []
        for c in s:
            if c != ')':
                stack.append(c)
            else:
                word = []
                while stack[-1] != '(':
                    word.append(stack.pop())
                stack.pop()
                bracketWord = ''.join(word[::-1])

                stack.append(
                    "?" if bracketWord not in knowledgeMap else knowledgeMap[bracketWord])

        return ''.join(stack)


s = "(name)is(age)yearsold"
knowledge = [["name", "bob"], ["age", "two"]]
print(Solution().evaluate(s, knowledge))
s = "hi(name)"
knowledge = [["a", "b"]]
print(Solution().evaluate(s, knowledge))
s = "(a)(a)(a)aaa"
knowledge = [["a", "yes"]]
print(Solution().evaluate(s, knowledge))
