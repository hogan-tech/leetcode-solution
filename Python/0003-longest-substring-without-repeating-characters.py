class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        string_list = []
        for char in s:
            if char in string_list:
                string_list = string_list[string_list.index(char)+1:]
            string_list.append(char)
            max_length = max(max_length, len(string_list))
        return max_length