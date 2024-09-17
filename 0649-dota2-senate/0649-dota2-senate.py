# time complexity: O(n)
# space complexity: O(n)
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        dQue = deque()
        rQue = deque()

        for i, s in enumerate(senate):
            if s == "R":
                rQue.append(i)
            else:
                dQue.append(i)

        while rQue and dQue:
            rTurn = rQue.popleft()
            dTurn = dQue.popleft()

            if dTurn < rTurn:
                dQue.append(dTurn + n)
            else:
                rQue.append(rTurn + n)

        return "Radiant" if rQue else "Dire"


senate = "RD"
print(Solution().predictPartyVictory(senate))
