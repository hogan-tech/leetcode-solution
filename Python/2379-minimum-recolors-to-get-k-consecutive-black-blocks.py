# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = float('inf')
        black = blocks[:k].count('B')
        if black == k:
            return 0
        result = min(result, k - black)
        left = 0
        for right in range(k, len(blocks)):
            left += 1
            if blocks[left-1] == 'B':
                black -= 1
            if blocks[right] == 'B':
                black += 1
            result = min(result, abs(k - black))

        return result


blocks = "WBBWWBBWBW"
k = 7
print(Solution().minimumRecolors(blocks, k))
blocks = "WBWBBBW"
k = 2
print(Solution().minimumRecolors(blocks, k))
blocks = "WBWW"
k = 2
print(Solution().minimumRecolors(blocks, k))
blocks = "WBB"
k = 1
print(Solution().minimumRecolors(blocks, k))
