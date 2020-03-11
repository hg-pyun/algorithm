/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    if(l1 === null && l2 === null) return null;
    
    const dummyHead = new ListNode();
    merge(l1, l2, dummyHead);
    
    return dummyHead.next;
};

function merge(l1, l2, head) { 
    if(l1 === null && l2 === null) return;
    
    if(l1 === null) {
        head.next = l2;
    }
    else if(l2 === null) {
        head.next = l1;
    }
    else if(l1.val < l2.val) {
        head.next = l1;
        merge(l1.next, l2, head.next);
    }
    else {
        head.next = l2;
        merge(l1, l2.next, head.next);
    }
}
