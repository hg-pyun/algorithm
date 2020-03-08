/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} val
 * @return {TreeNode}
 */
var searchBST = function(root, val) {
    return traversal(root, val) || null;
};

function traversal(node, val) {
    if(node === null) return;
    if(node.val === val) return node;
    
    const left = traversal(node.left, val);
    const right = traversal(node.right, val);
    
    return left || right;
}
