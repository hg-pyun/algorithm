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
var deepestLeavesSum = function(root) {
    
    const leafs = [];
    traversal(root, 0, leafs);
    
    const deepest = Math.max(...leafs.map((({depth}) => depth)));
    return leafs.filter(({depth}) => depth === deepest).map(({val}) => val).reduce((a, b) => a + b);
};

function traversal(node, depth, leafs) {
    if(node === null) 
        return;
    if(node.left === null && node.right === null)
        return leafs.push({depth, val: node.val});
    
    traversal(node.left, depth + 1, leafs);
    traversal(node.right, depth + 1, leafs);
}
