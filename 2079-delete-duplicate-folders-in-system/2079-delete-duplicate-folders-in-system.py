# time complexity: O(p*l*logl)
# space complexity: O(p*l)
from typing import Counter, List


class Trie:
    serial: str = ""
    children: dict

    def __init__(self):
        self.children = dict()


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie()

        for path in paths:
            cur = root
            for node in path:
                if node not in cur.children:
                    cur.children[node] = Trie()
                cur = cur.children[node]

        freq = Counter()

        def construct(node: Trie) -> None:
            if not node.children:
                return

            v = list()
            for folder, child in node.children.items():
                construct(child)
                v.append(folder + "(" + child.serial + ")")

            v.sort()
            node.serial = "".join(v)
            freq[node.serial] += 1

        construct(root)

        ans = list()
        path = list()

        def operate(node: Trie) -> None:
            if freq[node.serial] > 1:
                return
            if path:
                ans.append(path[:])

            for folder, child in node.children.items():
                path.append(folder)
                operate(child)
                path.pop()

        operate(root)
        return ans


paths = [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]
print(Solution().deleteDuplicateFolder(paths))
paths = [["a"], ["c"], ["a", "b"], ["c", "b"], [
    "a", "b", "x"], ["a", "b", "x", "y"], ["w"], ["w", "y"]]
print(Solution().deleteDuplicateFolder(paths))
paths = [["a", "b"], ["c", "d"], ["c"], ["a"]]
print(Solution().deleteDuplicateFolder(paths))
