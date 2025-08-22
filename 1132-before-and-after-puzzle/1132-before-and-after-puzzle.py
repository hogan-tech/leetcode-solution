# time complexity: O(n^2)
# space complexity: O(n)
from typing import List


class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        result = []
        phraseSet = set()
        for i in range(len(phrases)):
            for j in range(len(phrases)):
                if i != j:
                    if phrases[i].split(' ')[-1] == phrases[j].split(' ')[0]:
                        firstPhrases = phrases[i].split(' ')
                        secondPhrases = phrases[j].split(' ')
                        firstPhrases = firstPhrases[:len(firstPhrases) - 1]
                        concatPhrases = " ".join(firstPhrases + secondPhrases)
                        if concatPhrases not in phraseSet:
                            result.append(concatPhrases)
                            phraseSet.add(concatPhrases)
        result.sort()
        return result


phrases = ["writing code", "code rocks"]
print(Solution().beforeAndAfterPuzzles(phrases))
phrases = ["mission statement",
           "a quick bite to eat",
           "a chip off the old block",
           "chocolate bar",
           "mission impossible",
           "a man on a mission",
           "block party",
           "eat my words",
           "bar of soap"]
print(Solution().beforeAndAfterPuzzles(phrases))
phrases = ["a", "b", "a"]
print(Solution().beforeAndAfterPuzzles(phrases))
