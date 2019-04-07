/**
 * @param {number[]} A
 */
var RLEIterator = function (A) {
    this.seq = A;
    this.cursor = 0;
};

/**
 * @param {number} n
 * @return {number}
 */
RLEIterator.prototype.next = function (n) {
    if (this.seq[this.cursor] >= n) {
        this.seq[this.cursor] -= n;
        return this.seq[this.cursor + 1];
    } else {
        if (this.cursor + 2 > this.seq.length) return -1;

        const nextN = n - this.seq[this.cursor];
        this.cursor += 2;
        return this.next(nextN);
    }
};

/**
 * Your RLEIterator object will be instantiated and called as such:
 * var obj = new RLEIterator(A)
 * var param_1 = obj.next(n)
 */
