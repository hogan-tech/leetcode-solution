# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack = []  
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1] = (char, stack[-1][1] + 1)
            else:
                stack.append((char, 1))
            
            self.checkRemoval(stack, k)
        
        return ''.join(char * count for char, count in stack)
    
    def checkRemoval(self, stack: list, k: int):
        if len(stack) < 2:
            return
        
        if (stack[-2][0] == '(' and stack[-1][0] == ')' and 
            stack[-2][1] >= k and stack[-1][1] >= k):
            
            removeCount = min(stack[-2][1] // k, stack[-1][1] // k)
            
            stack[-2] = (stack[-2][0], stack[-2][1] - removeCount * k)
            stack[-1] = (stack[-1][0], stack[-1][1] - removeCount * k)
            
            if stack[-2][1] == 0:
                stack.pop(-2)
            if stack and stack[-1][1] == 0:
                stack.pop()
            
            if len(stack) >= 2:
                self.checkRemoval(stack, k)


s = "(())"
k = 1
print(Solution().removeSubstring(s, k))
s = "(()("
k = 1
print(Solution().removeSubstring(s, k))
s = "((()))()()()"
k = 3
print(Solution().removeSubstring(s, k))
