/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
var checkStraightLine = function(coordinates) {
    
    let beforeSlope;
    
    for(let i = 1; i < coordinates.length; i++) {
        const [x1, y1] = coordinates[i - 1];
        const [x2, y2] = coordinates[i];
        
        const curerntSlope = Math.abs((y2 - y1)/(x2 - x1));
        if(beforeSlope && beforeSlope !== curerntSlope) return false;
        beforeSlope = curerntSlope;
        
    }
    
    return true;
};
