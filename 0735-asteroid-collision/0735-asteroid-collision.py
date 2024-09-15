class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        stack = []
        for x in asteroids:
            if x > 0:
                stack.append(x)
            else:
                # negative asteroid destroys others in stack one by one
                while len(stack) > 0 and stack[-1] < abs(x):
                    stack.pop()
                # negative asteroid destroyed everyone
                if len(stack) == 0:
                    ans.append(x)
                # negative asteroid was beaten by positive asteroid (stack[-1])
                else:
                    # they destroyed each other
                    if stack[-1] == abs(x):
                        stack.pop()
        ans += stack
        return ans