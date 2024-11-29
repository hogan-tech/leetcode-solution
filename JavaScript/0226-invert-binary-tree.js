// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
}

/**
 * Inverts a binary tree.
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function (root) {
    if (!root) {
        return null;
    }
    // Swap the left and right children
    var temp = root.left;
    root.left = invertTree(root.right);
    root.right = invertTree(temp);
    return root;
};

/**
 * Prints the values of a binary tree in an inorder traversal.
 * @param {TreeNode} root
 * @return {string[]}
 */
function printBinaryTree(root) {
    if (root === null) {
        return [];
    }

    // Inorder traversal: left -> root -> right
    var result = [];
    result.push(root.val.toString());
    result = result.concat(printBinaryTree(root.left));
    result = result.concat(printBinaryTree(root.right));

    return result;
}

// Example usage:
var root = new TreeNode(4);
root.left = new TreeNode(2, new TreeNode(1), new TreeNode(3));
root.right = new TreeNode(7, new TreeNode(6), new TreeNode(9));

var result = invertTree(root);
var treeValues = printBinaryTree(result);
console.log(treeValues.join(" "));
