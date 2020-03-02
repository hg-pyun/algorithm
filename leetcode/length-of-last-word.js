/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    const lastWordLength = s.trim().split(" ").pop().length;
    return lastWordLength > 0 ? lastWordLength : 0;
};
