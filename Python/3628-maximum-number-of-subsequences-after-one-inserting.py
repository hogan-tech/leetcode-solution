# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)

        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + (1 if s[i - 1] == 'L' else 0)

        suffix = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + (1 if s[i] == 'T' else 0)

        count = 0
        for i in range(n):
            if s[i] == 'C':
                count += prefix[i] * suffix[i + 1]

        maxCount = count

        suffixCT = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            suffixCT[i] = suffixCT[i + 1]
            if s[i] == 'C':
                suffixCT[i] += suffix[i + 1]

        maxL = 0
        for k in range(n + 1):
            current = suffixCT[k]
            if current > maxL:
                maxL = current

        prefixLC = [0] * (n + 1)
        for i in range(1, n + 1):
            prefixLC[i] = prefixLC[i - 1]
            if i - 1 < n and s[i - 1] == 'C':
                prefixLC[i] += prefix[i - 1]

        maxT = 0
        for k in range(n + 1):
            current = prefixLC[k]
            if current > maxT:
                maxT = current

        maxC = 0
        for k in range(n + 1):
            lBefore = prefix[k]
            tAfter = suffix[k]
            current = lBefore * tAfter
            if current > maxC:
                maxC = current

        maxResult = max(maxL, maxT, maxC)
        maxCount = count + maxResult

        return maxCount if maxCount > 0 else 0


s = "LMCT"
print(Solution().numOfSubsequences(s))
s = "LCCT"
print(Solution().numOfSubsequences(s))
s = "L"
print(Solution().numOfSubsequences(s))
s = "CT"
print(Solution().numOfSubsequences(s))
