class Solution {
 public:
  int hammingWeight(uint32_t n) {
    int sum = 0, mask = 1;
    for (int i = 0; i < 32; i++) {
      if ((n & mask) != 0) sum++;
      n >>= 1;
    }
    return sum;
  }
};