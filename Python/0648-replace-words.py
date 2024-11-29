# time complexity: O(d*w + s*w^2)
# space complexity: O(d*w + s*w)
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictSet = set(dictionary)
        result = []
        for word in sentence.split(" "):
            for wordIdx in range(len(word)+1):
                if word[:wordIdx] in dictSet:
                    result.append(word[:wordIdx])
                    break
                if wordIdx == len(word):
                    result.append(word[:wordIdx])

        return " ".join(result)


dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(Solution().replaceWords(dictionary, sentence))
