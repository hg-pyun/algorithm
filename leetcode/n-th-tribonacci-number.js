/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) {
    const it = fibonacci(n);
    let ans = n;
    for (let i = 0; i <= n; i++) {
        ans = it.next().value;
    }
    
    return ans;
};

function* fibonacci(n){
    let count = 0
    let fn1 = 0;
    let fn2 = 1;
    let fn3 = 1;
    
    while (count <= n){
      count++
      let current = fn1;
      fn1 = fn2;
      fn2 = fn3;
      fn3 = current + fn1 + fn2
      yield current;
   }
}
