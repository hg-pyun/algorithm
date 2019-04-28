/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {

    let result = '';

    if (s.length === 1)
        return s;

    for (let l = 0; l < s.length; l++) {
        for (let r = s.length - 1; r > 0; r--) {
            if (s[l] === s[r]) {
                let subStr = s.substring(l, r + 1);
                if (checkPalindromic(subStr)) {
                    result = subStr.length > result.length ? subStr : result;
                    break;
                }
            }
        }
    }

    return result;
};

function checkPalindromic(s) {
    let leftCursor = 0;
    let rightCursor = s.length - 1;
    let isPalindromic = true;

    while (leftCursor < rightCursor) {
        if (s[leftCursor++] !== s[rightCursor--]) {
            isPalindromic = false;
            break;
        }
    }

    return isPalindromic;
}
