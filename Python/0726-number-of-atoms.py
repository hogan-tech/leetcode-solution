# time complexity: O(nlogn)
# space complexity: O(n)
from collections import defaultdict
import re


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        matcher = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        matcher.reverse()

        finalMap = defaultdict(int)

        stack = [1]

        running_mul = 1

        for atom, count, left, right, multiplier in matcher:
            if atom:
                if count:
                    finalMap[atom] += int(count) * running_mul
                else:
                    finalMap[atom] += 1 * running_mul

            elif right:
                if not multiplier:
                    multiplier = 1
                else:
                    multiplier = int(multiplier)
                running_mul *= multiplier
                stack.append(multiplier)

            elif left:
                running_mul //= stack.pop()

        finalMap = dict(sorted(finalMap.items()))

        ans = ""
        for atom in finalMap:
            ans += atom
            if finalMap[atom] > 1:
                ans += str(finalMap[atom])

        return ans


formula = "K4(ON(SO3)2)2"
print(Solution().countOfAtoms(formula))
