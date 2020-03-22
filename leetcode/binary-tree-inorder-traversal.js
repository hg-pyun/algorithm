/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    const r = [];
    inorder(root, r);
    
    return r;
};

function inorder(node, r) {
    if(node === null) return;
    
    inorder(node.left, r);
    r.push(node.val);
    inorder(node.right, r);
}
