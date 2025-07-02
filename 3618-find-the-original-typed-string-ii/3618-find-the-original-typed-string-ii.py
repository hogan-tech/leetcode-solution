# time complexity: O(n + k^2)
# space complexity: O(k)
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7
        n, count = len(word), 1
        freq = list()

        for i in range(1, n):
            if word[i] == word[i - 1]:
                count += 1
            else:
                freq.append(count)
                count = 1
        freq.append(count)

        result = 1
        for o in freq:
            result = result * o % mod

        if len(freq) >= k:
            return result

        _, g = [1] + [0] * (k - 1), [1] * k
        for i in range(len(freq)):
            fNew = [0] * k
            for j in range(1, k):
                fNew[j] = g[j - 1]
                if j - freq[i] - 1 >= 0:
                    fNew[j] = (fNew[j] - g[j - freq[i] - 1]) % mod
            gNew = [fNew[0]] + [0] * (k - 1)
            for j in range(1, k):
                gNew[j] = (gNew[j - 1] + fNew[j]) % mod
            _, g = fNew, gNew
        return (result - g[k - 1]) % mod


word = "aabbccdd"
k = 7
print(Solution().possibleStringCount(word, k))
word = "aabbccdd"
k = 8
print(Solution().possibleStringCount(word, k))
word = "aaabbb"
k = 3
print(Solution().possibleStringCount(word, k))
