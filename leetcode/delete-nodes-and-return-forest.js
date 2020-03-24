/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number[]} to_delete
 * @return {TreeNode[]}
 */
var delNodes = function(root, to_delete) {
    const r = [root];
    const queue = [root];
    
    let parent = null;
    
    while(queue.length !== 0) {
        const node = queue.shift();

        if(to_delete.includes(node.val)) {
            node.left && !to_delete.includes(node.left.val) && r.push(node.left);
            node.right && !to_delete.includes(node.right.val) && r.push(node.right);
        }

        node.left && queue.push(node.left);
        node.right && queue.push(node.right);
        
        if(node.left && to_delete.includes(node.left.val)) {
            node.left = null;
        }
        
        if(node.right && to_delete.includes(node.right.val)) {
            node.right = null;
        }
    }
    
    if(to_delete.includes(root.val)) {
        r.shift();
    }
    
    return r;
};
