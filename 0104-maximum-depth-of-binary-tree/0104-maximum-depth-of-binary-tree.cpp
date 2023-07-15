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
 public:
  int maxDepth(TreeNode *root) {
    if (root == NULL) return 0;
    queue<TreeNode *> q;
    q.push(root);
    int level = 0;
    while (!q.empty()) {
      int level_length = q.size();
      vector<int> levels;
      for (int i = 0; i < level_length; ++i) {
        TreeNode *current = q.front();
        q.pop();
        levels.push_back(current->val);
        if (current->left != NULL) q.push(current->left);
        if (current->right != NULL) q.push(current->right);
      }
      level++;
    }
    return level;
  }
};