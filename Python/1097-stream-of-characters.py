# time complexity: O(n)
# space complexity: O(n)
from collections import deque
from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque([])

        for word in set(words):
            node = self.trie
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)

        node = self.trie
        for ch in self.stream:
            if '$' in node:
                return True
            if not ch in node:
                return False
            node = node[ch]
        return '$' in node


streamChecker = StreamChecker(["cd", "f", "kl"])
print(streamChecker.query("a"))
print(streamChecker.query("b"))
print(streamChecker.query("c"))
print(streamChecker.query("d"))
print(streamChecker.query("e"))
print(streamChecker.query("f"))
print(streamChecker.query("g"))
print(streamChecker.query("h"))
print(streamChecker.query("i"))
print(streamChecker.query("j"))
print(streamChecker.query("k"))
print(streamChecker.query("l"))
