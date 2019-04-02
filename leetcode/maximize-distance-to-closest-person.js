/**
 * @param {number[]} seats
 * @return {number}
 */
var maxDistToClosest = function (seats) {
    let maxLength = 0;


    for (let i = 0; i < seats.length; i++) {
        let leftCursor = i;
        let rightCursor = i;
        let leftLength = 0;
        let rightLength = 0;

        if(seats[i] === 1) continue;

        while (leftCursor > 0 && seats[leftCursor--] !== 1) {
            leftLength++;
        }

        while (rightCursor < seats.length && seats[rightCursor++] !== 1) {
            rightLength++;
        }

        if(i === 0) {
            leftLength = 20001;
        }

        if(i === seats.length -1) {
            rightLength = 20001;
        }


        maxLength = Math.max(maxLength, Math.min(leftLength, rightLength));
    }

    return maxLength;
};
