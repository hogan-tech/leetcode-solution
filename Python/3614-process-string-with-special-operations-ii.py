# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def processStr(self, s: str, k: int) -> str:
        ops = []
        length = 0

        for ch in s:
            if ch == '#':
                length *= 2
                ops.append(('#', length))
            elif ch == '%':
                ops.append(('%', length))
            elif ch == '*':
                if length > 0:
                    length -= 1
                    ops.append(('*', length))
                else:
                    ops.append(('*', length))
            elif ch.isalpha():
                length += 1
                ops.append((ch, length))

        if k >= length:
            return '.'

        def findChar(i, k):
            while i >= 0:
                op, currLen = ops[i]
                prevLen = ops[i - 1][1] if i > 0 else 0
                if op == '#':
                    half = prevLen
                    if k >= currLen:
                        return '.'
                    if k >= half:
                        k -= half
                elif op == '%':
                    if k >= currLen:
                        return '.'
                    k = currLen - 1 - k
                elif op == '*':
                    if k >= currLen:
                        return '.'
                elif op.isalpha():
                    if k == currLen - 1:
                        return op
                i -= 1
            return '.'

        return findChar(len(ops) - 1, k)


s = "a#b%*"
k = 1
print(Solution().processStr(s, k))
s = "cd%#*#"
k = 3
print(Solution().processStr(s, k))
s = "z*#"
k = 0
print(Solution().processStr(s, k))
