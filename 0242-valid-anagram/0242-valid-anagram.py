# class Solution(object):
#     def isAnagram(self, s, t):
#         return sorted(s) == sorted(t)

class Solution(object):
    def isAnagram(self, s, t):
        return  collections.Counter(s) == collections.Counter(t)