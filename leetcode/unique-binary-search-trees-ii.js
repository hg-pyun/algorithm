/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number} n
 * @return {TreeNode[]}
 */
var generateTrees = function(n) {
    if (n == 0) return [];
    
    return recur(1, n);
};


function recur(start, end) {
    if (start > end) return [null];
    const res = [];
   
    for (let i = start; i <= end; i++) {
        const left = recur(start, i-1);
        const right = recur(i+1, end);
        
        for (const l of left) {
            for (const r of right) {
                const root = new TreeNode(i);
                root.left = l;
                root.right = r;
                res.push(root);
            }
        }
    }

  return res;
}
