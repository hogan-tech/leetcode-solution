/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
  void Inorder(TreeNode *current, vector<int> &output) {
    if (current) {
      Inorder(current->left, output);
      // cout << current->val << " ";
      output.push_back(current->val);
      Inorder(current->right, output);
    }
  }

 public:
  bool findTarget(TreeNode *root, int k) {
    vector<int> output;
    Inorder(root, output);
    int r = output.size() - 1;
    int l = 0;
    int sum = 0;
    while (l < r) {
      sum = output[l] + output[r];
      if (sum == k) return true;
      if (sum > k) {
        r--;
      } else {
        l++;
      }
    }
    return false;
  }
};