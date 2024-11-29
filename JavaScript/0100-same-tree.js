/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */

var isSameTree = function (p, q) {
	if (p === null && q === null)
		return true;
	if (p === null || q === null)
		return false;
	if (p.val !== q.val)
		return false;
	return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};

// Example usage:
var p = new TreeNode(1);
p.left = new TreeNode(2);
p.right = new TreeNode(2);

var q = new TreeNode(1);
q.left = new TreeNode(2);
q.right = new TreeNode(2);

console.log(isSameTree(p, q));
