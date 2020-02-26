/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */
var countCharacters = function(words, chars) {
    
    let result = 0;
    
    while(words.length > 0) {
        const word = words.pop();
        const count = checkInclude(word, chars);
        if(count) result += count;
    }
    
    return result;
};

function checkInclude(word, chars) {
    let count = 0;
    const arrChars = [...chars];
    
    for(let i = 0; i < word.length; i++) {
        const c = word[i];
        const j = arrChars.indexOf(c);
        
        if(j === -1) {
            return false;
        }
        else {
            arrChars[j] = '';
            count++;
        }
    }
    return count;
}
