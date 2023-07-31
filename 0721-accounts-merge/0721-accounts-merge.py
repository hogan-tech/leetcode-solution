from typing import List


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
            account_first_email = account[1]
            self.adjacent.setdefault(account_first_email, [])
            for email in account[2:]:
                self.adjacent.setdefault(email, [])
                self.adjacent[account_first_email].append(email)
                self.adjacent[email].append(account_first_email)

        merged_accounts = []
        for account in account_list:
            account_name = account[0]
            account_first_email = account[1]

            if account_first_email not in self.visited:
                merged_account = []
                merged_account.append(account_name)
                self.DFS(merged_account, account_first_email)
                merged_account[1:] = sorted(merged_account[1:])
                merged_accounts.append(merged_account)

        return merged_accounts