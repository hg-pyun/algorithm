/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    return reverse(head, null);
};

function reverse(currentNode, beforeNode) {
    if(currentNode === null) return beforeNode;
    
    const temp = currentNode.next;
    currentNode.next = beforeNode;
    return reverse(temp, currentNode);
}
