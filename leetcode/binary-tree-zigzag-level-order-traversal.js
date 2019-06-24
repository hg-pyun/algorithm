/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var zigzagLevelOrder = function(root) {
    
    if(!root) return [];
    
    const queue = [root];
    const ans = [];
    let isReverse = true;
    
    while(queue.length !== 0) {
        let count = queue.length;
        const subArray = [];
        while(count > 0) {
            const cNode = queue.shift();
            count--;
            subArray.push(cNode.val);
            
            if(cNode.left)
                queue.push(cNode.left);
            if(cNode.right)
                queue.push(cNode.right);
        }
        
        if(isReverse = !isReverse)
            subArray.reverse();
        
        ans.push(subArray);
    }
    
    return ans;
};
