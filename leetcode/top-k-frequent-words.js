/**
 * @param {string[]} words
 * @param {number} k
 * @return {string[]}
 */
var topKFrequent = function(words, k) {
   
    const map = {};
    
    for(let i = 0; i < words.length; i++) {
        const word = words[i];
        map[word] = map[word] ? ++map[word] : 1;
    }
    
    const countMap = {};
    
    for(const key in map) {
        const v = map[key];
        if(countMap[v]) {
            countMap[v].push(key);
        }
        else {
            countMap[v] = [key];
        }
    }
    
    console.log(countMap);
    const countOrder = [];
    
    for(const count in countMap) {
        const data = countMap[count].sort();
        countOrder.push({
            count,
            data, 
        })
    }
        
    countOrder.sort((a, b) => b.count - a.count);    
    
    const result = [];
    let index = 0;
    
    while(k > 0) {
        const data = countOrder[index].data;
        for(let i = 0; i < data.length; i++) {
            result.push(data[i]);
            k--;
            if(k === 0) break;
        }
        index++;
    }
    
    return result;
};
