/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    return traversal(root, 0)
};

function traversal(node, depth) {
    if(node === null) return depth;
    const left = traversal(node.left, depth + 1);
    const right = traversal(node.right, depth + 1);
    
    return Math.max(left, right);
}
