class Solution {
  bool matches(int map1[],int map2[]){
    for(int i = 0;i < 26;i ++){
      if(map1[i] != map2[i]){
        return false;
      }
    }
    return true;
  }
 public:
  bool checkInclusion(string s1, string s2) {
    if (s1.length() > s2.length()) return false;
    int map1[26] = {0};
    for (int i = 0; i < s1.length(); i++) {
      map1[s1[i] - 'a']++;
    }
    for (int i = 0; i <= s2.length() - s1.length(); i++) {
      int map2[26] = {0};
      for (int j = 0; j <  s1.length(); j++) {
        map2[s2[i+j] - 'a']++;
      }
      if(matches(map1,map2)){
        return true;
      }
    }
    return false;
  }
};