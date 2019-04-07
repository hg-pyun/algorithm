/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function (s) {
    const stack = [];

    let numberAssembler = [];
    for (let i = 0; i < s.length; i++) {
        const char = s[i];

        // 들어오는 문자열이 숫자일 경우 조합한다. ex) 100[leetcode] 형태
        if(!isNaN(char)) {
            numberAssembler.push(char);
        }
        else if (char === '[') {
            stack.push(numberAssembler.join(''));
            numberAssembler = [];
        }
        // ']' 문자열을 만날 경우, stack에 저장해뒀던 문자열을 꺼내 조합하여 반복한다.
        else if(char === ']') {
            let repeatChars = [];
            let cursor;
            let count;

            while(1) {
                cursor = stack.pop();

                if(isNaN(cursor)) {
                    repeatChars.push(cursor);
                }
                else {
                    count = parseInt(cursor);
                    break;
                }
            }

            stack.push(repeatChars.reverse().join('').repeat(count));
        }
        else {
            stack.push(char);
        }
    }

    return stack.join('');
};
