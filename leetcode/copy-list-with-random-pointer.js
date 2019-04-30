/**
 * // Definition for a Node.
 * function Node(val,next,random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */
/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function(head) {
    
    if(head === null) return head;
    
    const map = new Map();
    const list = [];
    
    let currentNode = head;
    while(1) {
        let copyNode = new Node(currentNode.val, null, null);
        map.set(currentNode, copyNode);
        list.push(copyNode);
        if(currentNode.next === null) break;
        currentNode = currentNode.next;
    } 
    
    let i = 0;
    currentNode = head;
    while(i < list.length) {
        if(currentNode.next !== null) {
            list[i].next = list[i+1];
        }
        list[i].random = map.get(currentNode.random) || null;
        
        currentNode = currentNode.next;
        i++;
    }

    return list[0];
};
