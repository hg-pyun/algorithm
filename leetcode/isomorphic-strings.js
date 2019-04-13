/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

var isIsomorphic = function (s, t) {

    const sData = {
        map: new Map(),
        arr: [],
        count: -1
    };

    const tData = {
        map: new Map(),
        arr: [],
        count: -1
    };

    for (let i = 0; i < s.length; i++) {
        const sChar = s[i];
        const tChar = t[i];
        makeIndexArr(sData, sChar);
        makeIndexArr(tData, tChar);
    }

    for (let i = 0; i < s.length; i++) {
        if (sData.arr[i] !== tData.arr[i]) return false;
    }

    return true;
};

function makeIndexArr(data, char) {
    if (!data.map.has(char)) {
        data.map.set(char, data.count++);
        data.arr.push(data.count);
    } else {
        data.arr.push(data.map.get(char));
    }
}
