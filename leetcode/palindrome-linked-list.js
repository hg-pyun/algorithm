/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    
    let current = head;
    let length = 0;
    while(current !== null) {
        length++;
        current = current.next;
    }
    
    let c = 0;
    current = head;
    let prev = null;
    let next = null;
    
    while(c < length/2) {
        next = current.next;
        current.next = prev;
        prev = current;
        current = next;
        c++;
    }
    
    if(length%2 !== 0) {
        prev = prev.next;
    }
        
    let result = true;
    while(current !== null && prev !== null) {
        if(current.val !== prev.val) {
            result = false;
            break;
        };
        
        current = current.next;
        prev = prev.next;
    }
    
    return result;
};
