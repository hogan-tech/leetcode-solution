class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        filteredList = [item for item in list(s.split(" ")) if item != ""]
        return len(filteredList[-1])


s = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(s))
