from typing import Counter, List


class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        left = 0

        for right in range(1, len(chars)+1):
            if right < len(chars) and chars[right-1] == chars[right]:
                count += 1
            else:
                chars[left] = chars[right-1]
                left += 1
                if count > 1:
                    for c in str(count):
                        chars[left] = c
                        left += 1
                count = 1

        return left


chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(Solution().compress(chars))
