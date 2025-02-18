# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        stack = []
        for i in range(len(pattern) + 1):
            stack.append(i + 1)
            if i == len(pattern) or pattern[i] == 'I':
                while stack:
                    result.append(str(stack.pop()))
        return ''.join(result)


pattern = "IIIDIDDD"
print(Solution().smallestNumber(pattern))
pattern = "DDD"
print(Solution().smallestNumber(pattern))
