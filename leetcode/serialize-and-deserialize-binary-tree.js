/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
var serialize = function(root) {
    const valueArr = levelOrder(root);
    return `[${valueArr.join(',')}]`;
};

function levelOrder(node) {
    const queue = [node];
    const values = [];
    let lastExistNodeIndex = 0;
    let index = 0;
    while(queue.length !== 0) {
        let currentNode = queue.shift();
        if(currentNode) {
            lastExistNodeIndex = index + 1;
            values.push(currentNode.val);
            queue.push(currentNode.left);
            queue.push(currentNode.right);
        }
        else {
            values.push('null');
        }
        index++;
    }
    
    return values.slice(0, lastExistNodeIndex);
}

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
var deserialize = function(data) {
    const treeNodes = JSON.parse(data).map(value => value === null ? null : new TreeNode(value));
    if(treeNodes.length === 0) return null;
    
    const root = treeNodes.shift();
    const queue = [root];
    while(queue.length) {
        const node = queue.shift();
        node.left = treeNodes.shift();
        node.right = treeNodes.shift();
        if(node.left) queue.push(node.left);
        if(node.right) queue.push(node.right);
    }
    
    return root;
};

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */
