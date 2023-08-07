from typing import List


class Codec:
    def __init__(self) -> None:
        self.stringIndex = []
        pass

    def encode(self, strs: List[str]) -> str:
        encodeString = ""
        for string in strs:
            currentIndex = len(string)
            self.stringIndex.append(currentIndex)
            encodeString += string
        print(self.stringIndex)
        return encodeString

    def decode(self, s: str) -> List[str]:
        decodeList = []
        for i,item in enumerate(self.stringIndex):
            decodeList.append(s[:item])
            s = s[item:]
        return decodeList