/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
 public:
  Node* connect(Node* root) {
    if (root == NULL) return root;
    queue<Node*> q;
    q.push(root);
    int size = 0;
    while (!q.empty()) {
      size = q.size();
      for (int i = 0; i < size; i++) {
        Node* current = q.front();
        q.pop();
        cout << current->val << " ";
        if (i < size - 1) {
          current->next = q.front();
        }
        if (current->left != NULL) q.push(current->left);
        if (current->right != NULL) q.push(current->right);
      }
    }
    return root;
  }
};