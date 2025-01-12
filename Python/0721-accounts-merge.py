from collections import defaultdict
from typing import List

# time complexity: O(nklognk)
# space complexity: O(nk)
class Solution:
    def __init__(self):
        self.visited = set()
        self.adjacent = {}

    def DFS(self, merged_account: List[str], email: str) -> None:
        self.visited.add(email)
        merged_account.append(email)

        for neighbor in self.adjacent[email]:
            if neighbor not in self.visited:
                self.DFS(merged_account, neighbor)

    def accountsMerge(self, account_list: List[List[str]]) -> List[List[str]]:
        for account in account_list:
            accountFirstEmail = account[1]
            self.adjacent.setdefault(accountFirstEmail, [])
            for email in account[2:]:
                self.adjacent.setdefault(email, [])
                self.adjacent[accountFirstEmail].append(email)
                self.adjacent[email].append(accountFirstEmail)

        mergedAccounts = []
        for account in account_list:
            accountName = account[0]
            accountFirstEmail = account[1]

            if accountFirstEmail not in self.visited:
                mergedAccount = []
                mergedAccount.append(accountName)
                self.DFS(mergedAccount, accountFirstEmail)
                mergedAccount[1:] = sorted(mergedAccount[1:])
                mergedAccounts.append(mergedAccount)

        return mergedAccounts

# time complexity: O(nk*a(n)) + O(mklogk)
# space complexity: O(nk)
class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
    
    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parents[rootX] = rootY
            

class Solution:
    def accountsMerge(self, accountList: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accountList))
        emailMapping = {}
        for i, account in enumerate(accountList):
            name = account[0]
            emails = account[1:]
            for email in emails:
                if email in emailMapping:
                    if name != accountList[emailMapping[email]][0]:
                        return
                    uf.union(emailMapping[email], i)
                emailMapping[email] = i
                
        mergedAccounts = defaultdict(list)
        for email, ids in emailMapping.items():
            mergedAccounts[uf.find(ids)].append(email)
        
        finalMerged = []
        for parent, emails in mergedAccounts.items():
            finalMerged.append([accountList[parent][0]] + sorted(emails))
            
        return finalMerged

Accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]

print(Solution().accountsMerge(Accounts))
