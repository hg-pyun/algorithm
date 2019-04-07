/**
 * @param {string} s
 * @param {string[]} d
 * @return {string}
 */
var findLongestWord = function (s, d) {

    let resultList = [];

    d.forEach((word) => {
        let cursor = 0;
        for (let i = 0; i < s.length; i++) {
            const char = s[i];

            if (char === word[cursor]) {
                cursor++;
            }
        }

        if (cursor === word.length) {
            resultList.push(word);
        }
    });

    resultList.sort();
    return getMaxLengthWord(resultList);
};

function getMaxLengthWord(list) {
    let maxLengthWord = '';

    list.forEach((word) => {
        if(word.length > maxLengthWord.length) {
            maxLengthWord = word;
        }
    });

    return maxLengthWord;
}
