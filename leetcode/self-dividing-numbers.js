/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    const r = [];
    
    for(let i = left; i <= right; i++) {
        check(i) && r.push(i);
    }
    
    return r;
};

function check(num) {
  const digits = [];
  let dNum = num;
  let start = false;
  for(let i = 10000; i >= 1; i /= 10) {
      const q = Math.floor(dNum/i);
      if(start && q === 0) return false;
      if(q !== 0) {
          digits.push(q);
          dNum = dNum % i;
          start = true;
      }
  }

  for(let i = 0; i < digits.length; i++) {
    if(num % digits[i] !== 0) return false;
  }

  return true;
}
