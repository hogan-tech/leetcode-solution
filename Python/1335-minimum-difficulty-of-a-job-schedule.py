# time complexity: O(n^2 * d)
# space complexity: O(n*d)
class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d:
            return -1

        minDiffPrevDay, minDiffCurrDay = [
            float('inf')] * n, [float('inf')] * n

        for day in range(d):
            stack = []

            for i in range(day, n):

                if i == 0:
                    minDiffCurrDay[i] = jobDifficulty[0]
                else:
                    minDiffCurrDay[i] = minDiffPrevDay[i -
                                                       1] + jobDifficulty[i]

                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[i]:

                    j = stack.pop()
                    diff_incr = jobDifficulty[i] - jobDifficulty[j]
                    minDiffCurrDay[i] = min(
                        minDiffCurrDay[i], minDiffCurrDay[j] + diff_incr)

                if stack:
                    minDiffCurrDay[i] = min(
                        minDiffCurrDay[i], minDiffCurrDay[stack[-1]])

                stack.append(i)

            minDiffPrevDay, minDiffCurrDay = minDiffCurrDay, minDiffPrevDay

        return minDiffPrevDay[-1]


jobDifficulty = [6, 5, 4, 3, 2, 1]
d = 2
print(Solution().minDifficulty(jobDifficulty, d))
