# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target != 1:
            if target % 2 == 0 and maxDoubles != 0:
                target /= 2
                maxDoubles -= 1
                count += 1
            else:
                if maxDoubles == 0:
                    count += (target - 1)
                    target = 1
                else:
                    target -= 1
                    count += 1

        return int(count)


target = 5
maxDoubles = 0
print(Solution().minMoves(target, maxDoubles))
target = 19
maxDoubles = 2
print(Solution().minMoves(target, maxDoubles))
target = 10
maxDoubles = 4
print(Solution().minMoves(target, maxDoubles))
target = 656101987
maxDoubles = 1
print(Solution().minMoves(target, maxDoubles))
