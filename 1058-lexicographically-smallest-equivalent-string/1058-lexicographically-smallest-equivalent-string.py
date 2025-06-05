# time complexity: O((len(s)+len(base)) * log26)
# space complexity: O(26)

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX < parentY:
            self.parent[parentY] = parentX
        else:
            self.parent[parentX] = parentY
        return

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        unionFind = UnionFind(26)
        for i in range(len(s1)):
            ordC1 = ord(s1[i]) - ord('a')
            ordC2 = ord(s2[i]) - ord('a')
            unionFind.union(ordC1, ordC2)

        result = ""
        for c in baseStr:
            ordC = ord(c) - ord('a')
            currParent = unionFind.find(ordC)
            result += chr(currParent + ord('a'))
        return result


'''
[m,p], [a,o], [k,r,s], [e,i].
So the answer is "makkek".
'''
s1 = "parker"
s2 = "morris"
baseStr = "parser"
print(Solution().smallestEquivalentString(s1, s2, baseStr))
s1 = "hello"
s2 = "world"
baseStr = "hold"
print(Solution().smallestEquivalentString(s1, s2, baseStr))
s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"
print(Solution().smallestEquivalentString(s1, s2, baseStr))
