/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParity = function(A) {

    let cur = 0;
    for(let i = 0; i < A.length; i++) {
        if(A[i] % 2 === 0) {
            const temp = A[cur];
            A[cur] = A[i];
            A[i] = temp;
            cur++;
        }
    }
    
    return A;
};
