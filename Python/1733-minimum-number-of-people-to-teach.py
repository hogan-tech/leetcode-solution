# time complexity: O(n*m)
# space complexity: O(n*n)
from collections import Counter
from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(language) for language in languages]
        dontSpeak = set()
        for u, v in friendships:
            u = u - 1
            v = v - 1
            if languages[u] & languages[v]:
                continue
            dontSpeak.add(u)
            dontSpeak.add(v)

        langCount = Counter()
        for ppl in dontSpeak:
            for language in languages[ppl]:
                langCount[language] += 1
        return 0 if not dontSpeak else len(dontSpeak) - max(list(langCount.values()))


n = 2
languages = [[1], [2], [1, 2]]
friendships = [[1, 2], [1, 3], [2, 3]]
print(Solution().minimumTeachings(n, languages, friendships))
n = 3
languages = [[2], [1, 3], [1, 2], [3]]
friendships = [[1, 4], [1, 2], [3, 4], [2, 3]]
print(Solution().minimumTeachings(n, languages, friendships))
'''
a b
[a], [b], [a,b]
1[a] <-> 2[b]
1[a] <-> 3[a,b]
2[b] <-> 3[a,b]
'''
