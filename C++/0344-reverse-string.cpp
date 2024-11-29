class Solution {
 public:
  void reverseString(vector<char>& s) {
    char temp = '\0';
    for (int i = 0; i < (s.size() / 2); i++) {
      temp = s[i];
      s[i] = s[s.size() - i - 1];
      s[s.size() - i - 1] = temp;
    }
  }
};