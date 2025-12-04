# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def countCollisions(self, directions: str) -> int:
        result = 0
        flag = -1

        for dir in directions:
            if dir == "L":
                if flag >= 0:
                    result += flag + 1
                    flag = 0
            elif dir == "S":
                if flag > 0:
                    result += flag
                flag = 0
            else:
                if flag >= 0:
                    flag += 1
                else:
                    flag = 1
        return result


directions = "RLRSLL"
print(Solution().countCollisions(directions))
directions = "LLRR"
print(Solution().countCollisions(directions))
