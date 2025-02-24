# time complexity: O(nlogn)
# space compelxity: O(n)
from collections import defaultdict
from itertools import combinations
from typing import Counter, List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        patternList = []
        userDict = defaultdict(list)
        for i in range(len(username)):
            patternList.append([timestamp[i], username[i], website[i]])
        patternList.sort()
        for _, username, website in patternList:
            userDict[username].append(website)

        counter = Counter()
        for username, websites in userDict.items():
            counter.update(Counter(set(combinations(websites, 3))))

        return max(sorted(counter), key=counter.get)


username = ["joe", "joe", "joe", "james", "james",
            "james", "james", "mary", "mary", "mary"]
timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
website = ["home", "about", "career", "home", "cart",
           "maps", "home", "home", "about", "career"]
print(Solution().mostVisitedPattern(username, timestamp, website))
username = ["ua", "ua", "ua", "ub", "ub", "ub"]
timestamp = [1, 2, 3, 4, 5, 6]
website = ["a", "b", "a", "a", "b", "c"]
print(Solution().mostVisitedPattern(username, timestamp, website))
