class Solution {
 public:
  vector<string> letterCasePermutation(string S) {
    vector<string> output;
    output.push_back("");

    for (int i = 0; i < S.length(); i++) {
      if (isalpha(S[i])) {
        vector<string> temp;
        for (auto o : output) {
          temp.push_back(o + (char)toupper(S[i]));
          temp.push_back(o + (char)tolower(S[i]));
        }
        output = temp;
      } else {
        for (auto &o : output) {
          o += S[i];
        }
      }
    }
    return output;
  }
};