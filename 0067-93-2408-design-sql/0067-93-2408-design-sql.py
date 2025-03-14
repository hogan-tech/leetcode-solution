from typing import List


class TableNode():
    def __init__(self, columns):
        self.rowId = 0
        self.total_columns = columns
        self.rows = {}


class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {}
        for name, column in zip(names, columns):
            node = TableNode(column)
            self.tables[name] = node

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.tables:
            return False
        node = self.tables[name]
        if node.total_columns != len(row):
            return False
        node.rowId += 1
        node.rows[node.rowId] = row
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name in self.tables:
            node = self.tables[name]
            if rowId <= node.rowId and rowId in node.rows:
                del node.rows[rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables:
            return "<null>"
        node = self.tables[name]
        if rowId not in node.rows or columnId < 1 or columnId > node.total_columns:
            return "<null>"
        else:
            return node.rows[rowId][columnId-1]

    def exp(self, name: str) -> List[str]:
        if name not in self.tables:
            return []
        else:
            res = []
            node = self.tables[name]
            for key in node.rows.keys():
                s = str(key)+',' + ','.join(node.rows[key])
                res.append(s)
            return res


sql = SQL(["one", "two", "three"], [2, 3, 1])
print(sql.ins("two", ["first", "second", "third"]))
print(sql.sel("two", 1, 3))
print(sql.ins("two", ["fourth", "fifth", "sixth"]))
print(sql.exp("two"))
print(sql.rmv("two", 1))
print(sql.sel("two", 2, 2))
print(sql.exp("two"))
