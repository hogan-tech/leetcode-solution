class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in ransomNote:
            if (c not in magazine):
                return False
            location = magazine.index(c)
            magazine = magazine[:location] + magazine[location+1:]
        return True