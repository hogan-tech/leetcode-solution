/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    function longestPath(node) {
        if (!node) {
            return 0;
        }
        var leftPath = longestPath(node.left);
        var rightPath = longestPath(node.right);
        return Math.max(leftPath, rightPath) + 1;
    }

    return longestPath(root);
};
