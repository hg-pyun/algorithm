/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
     reverse(s, 0, s.length - 1);
};

function reverse(s, i, j) {
    if(i >= j) return;
    
    const temp = s[i];
    s[i] = s[j];
    s[j] = temp;
    
    reverse(s, i + 1, j - 1);
}
