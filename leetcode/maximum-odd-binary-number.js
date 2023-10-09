/**
 * @param {string} s
 * @return {string}
 */
var maximumOddBinaryNumber = function(s) {
    let sCount = 0;

    [...s].forEach((char) => char === "1" && sCount++);
    
    let ans = ""

    for (let i = 1; i < s.length; i++) {
        if(sCount > 1) {
            ans += "1"
            sCount -= 1
        }
        else {
            ans += "0"
        }
    }

    return ans += "1"
};
