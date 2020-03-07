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
var swapPairs = function(head) {
    return swap(head);
}
function swap(node) {
    if(node === null || node.next === null) return node;
    const temp = node.next;
    node.next = temp.next;
    temp.next = node;
    node.next = swap(node.next);
    return temp;
}
