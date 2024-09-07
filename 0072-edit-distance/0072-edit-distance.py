# time complexity: O(m*n)
# space complexity: O(m*n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [
            [None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)
        ]

        def minDistanceRecur(word1, word2, word1Index, word2Index):
            if word1Index == 0:
                return word2Index
            if word2Index == 0:
                return word1Index
            if memo[word1Index][word2Index] is not None:
                return memo[word1Index][word2Index]
            minEditDistance = 0
            if word1[word1Index - 1] == word2[word2Index - 1]:
                minEditDistance = minDistanceRecur(
                    word1, word2, word1Index - 1, word2Index - 1
                )
            else:
                insertOperation = minDistanceRecur(
                    word1, word2, word1Index, word2Index - 1
                )
                deleteOperation = minDistanceRecur(
                    word1, word2, word1Index - 1, word2Index
                )
                replaceOperation = minDistanceRecur(
                    word1, word2, word1Index - 1, word2Index - 1
                )
                minEditDistance = (
                    min(insertOperation, deleteOperation, replaceOperation) + 1
                )
            memo[word1Index][word2Index] = minEditDistance
            return minEditDistance

        return minDistanceRecur(word1, word2, len(word1), len(word2))


word1 = "horse"
word2 = "ros"
print(Solution().minDistance(word1, word2))
