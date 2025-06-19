# time complexity: O(n)
# space complexity: O(n)
from typing import List


class Codec:
    def __init__(self):
        self.idxList = []

    def encode(self, strs: List[str]) -> str:
        encodeString = ''
        for string in strs:
            self.idxList.append(len(string))
            encodeString += string
        return encodeString

    def decode(self, s: str) -> List[str]:
        decodeList = []
        for wordIdx in self.idxList:
            decodeList.append(s[:wordIdx])
            s = s[wordIdx:]
        return decodeList

codec = Codec()
print(codec.encode(["Hello", "World"]))
print(codec.decode("HelloWorld"))
