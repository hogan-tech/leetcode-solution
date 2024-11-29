/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val === undefined ? 0 : val)
 *     this.left = (left === undefined ? null : left)
 *     this.right = (right === undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function (root, subRoot) {
	function isSameTree(root1, root2) {
		if (!root1 && !root2) {
			return true;
		}
		if (!root1 || !root2) {
			return false;
		}
		if (root1.val !== root2.val) {
			return false;
		}
		return isSameTree(root1.left, root2.left) && isSameTree(root1.right, root2.right);
	}

	function dfs(node) {
		if (!node) {
			return false;
		} else if (isSameTree(node, subRoot)) {
			return true;
		}
		return dfs(node.left) || dfs(node.right);
	}

	return dfs(root);
};

// Example usage:
var root = new TreeNode(3);
root.left = new TreeNode(4);
root.left.left = new TreeNode(1);
root.left.right = new TreeNode(2);
root.right = new TreeNode(5);

var subRoot = new TreeNode(4);
subRoot.left = new TreeNode(1);
subRoot.right = new TreeNode(2);

console.log(isSubtree(root, subRoot));
