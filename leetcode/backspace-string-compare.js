/**
 * @param {string} S
 * @param {string} T
 * @return {boolean}
 */
var backspaceCompare = function (S, T) {
    return parseBackspace(S) === parseBackspace(T);
};


function parseBackspace(strings) {
    const stack = [];

    for(let i=0; i<strings.length; i++) {
        const char = strings[i];
        if(char === '#')
            stack.pop(char);
        else
            stack.push(char);
    }

    return stack.join('');
}
