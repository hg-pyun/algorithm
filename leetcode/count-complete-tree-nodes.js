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

let count;
var countNodes = function(root) {
    count = 0;
    if(!root) {
        return 0;
    }
    traversal(root);
    return count;
};

const traversal = function(node) {
    if(node) {
         traversal(node.left);
         traversal(node.right);
         count++;
    }
    return;
}
