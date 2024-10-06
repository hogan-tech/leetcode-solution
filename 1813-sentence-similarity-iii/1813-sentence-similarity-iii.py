# time complexity: O(m+n)
# space complexity: O(m+n)
from collections import deque


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        queue1 = deque(sentence1.split())
        queue2 = deque(sentence2.split())
        while queue1 and queue2 and queue1[0] == queue2[0]:
            queue1.popleft()
            queue2.popleft()
        while queue1 and queue2 and queue1[-1] == queue2[-1]:
            queue1.pop()
            queue2.pop()

        return not queue1 or not queue2


sentence1 = "Eating right now"
sentence2 = "Eating"
print(Solution().areSentencesSimilar(sentence1, sentence2))
