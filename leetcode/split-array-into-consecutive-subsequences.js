/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isPossible = function (nums) {
  let count = {}, tail = {};

  for (let n of nums) {
    count[n] = count[n] ? count[n] + 1 : 1;
  }

  for (let n of nums) {
    if (count[n] === 0) {
      continue;
    } else if (tail[n] > 0) {
      tail[n] -= 1;
      tail[n + 1] = tail[n + 1] ? tail[n + 1] + 1 : 1
    } else if (count[n + 1] > 0 && count[n + 2] > 0) {
      count[n + 1] -= 1;
      count[n + 2] -= 1;
      tail[n + 3] = tail[n + 3] ? tail[n + 3] + 1 : 1
    } else {
      return false
    }
    count[n] -= 1
  }
  return true
};
