class Solution {
 public:
  int lengthOfLongestSubstring(string s) {
    vector<int> chars(128);
    int left = 0, right = 0, res = 0;
    while (right < s.length()) {
      chars[s[right]]++;
      while (chars[s[right]] > 1) {
        chars[s[left]]--;
        left++;
      }
      res = max(res, right - left + 1);
      right++;
    }
    return res;
  }
};