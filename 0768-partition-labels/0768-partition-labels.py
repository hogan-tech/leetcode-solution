class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {c: i for i, c in enumerate(s)}

        partitionEnd = 0
        partitionStart = 0
        partitionSize = []

        for i, c in enumerate(s):
            partitionEnd = max(partitionEnd, lastIdx[c])
            if i == partitionEnd:
                partitionSize.append(partitionEnd - partitionStart + 1)
                partitionStart = partitionEnd + 1
        return partitionSize