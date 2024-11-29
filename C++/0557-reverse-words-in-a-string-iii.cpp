class Solution {
  void reverseString(vector<char>& s) {
    char temp = '\0';
    for (int i = 0; i < (s.size() / 2); i++) {
      temp = s[i];
      s[i] = s[s.size() - i - 1];
      s[s.size() - i - 1] = temp;
    }
  }

 public:
  string reverseWords(string s) {
    vector<char> words;
    string output;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] != ' ') {
        words.push_back(s[i]);
      }
      if (s[i] == ' ') {
        reverseString(words);
        output.insert(output.end(), words.begin(), words.end());
        output.insert(output.end(), ' ');
        words.clear();
      }
      if (i == s.size() - 1) {
        reverseString(words);
        output.insert(output.end(), words.begin(), words.end());
      }
    }
    return output;
  }
};