# time complexity: O(n)
# space complexity: O(1)
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)
        for key, freq in magazineCounter.items():
            if key in ransomNoteCounter:
                ransomNoteCounter[key] -= freq
                if ransomNoteCounter[key] <= 0:
                    del ransomNoteCounter[key]
        return len(ransomNoteCounter) == 0


ransomNote = "a"
magazine = "b"
print(Solution().canConstruct(ransomNote, magazine))
ransomNote = "aa"
magazine = "ab"
print(Solution().canConstruct(ransomNote, magazine))
ransomNote = "aa"
magazine = "aab"
print(Solution().canConstruct(ransomNote, magazine))
