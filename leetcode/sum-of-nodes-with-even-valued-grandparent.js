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
var sumEvenGrandparent = function(root) {
    const result = [];
    traversal(root, result);
    
    return result.length === 0 ? 0 : result.reduce((a, b) => a + b);
};

function traversal(node, result) {
    if(node === null) return;
    if(node.val % 2 === 0) {
        traversalEdgeNode(node, result, 0);
    }
    
    traversal(node.left, result);
    traversal(node.right, result);
}

function traversalEdgeNode(node, result, step) {
    if(node === null) return;
    if(step === 2) return result.push(node.val);
    
    traversalEdgeNode(node.left, result, step + 1);
    traversalEdgeNode(node.right, result, step + 1);
}
