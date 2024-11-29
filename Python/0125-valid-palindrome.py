class Solution(object):
    def isPalindrome(self, s):
        filter_str = filter(lambda ch: ch.isalnum(), s)
        lower_str = map(lambda ch: ch.lower(), filter_str)
        list_str = list(lower_str)
        reverse_str = list_str[::-1]
        return reverse_str == list_str