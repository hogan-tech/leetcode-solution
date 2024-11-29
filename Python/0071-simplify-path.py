# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for item in path.split("/"):
            if item:
                if item == "..":
                    if stack:
                        stack.pop()
                elif item == ".":
                    continue
                else:
                    stack.append(item)
        return "/" + "/".join(stack)


path = "/a/./b/../../c/"
print(Solution().simplifyPath(path))
