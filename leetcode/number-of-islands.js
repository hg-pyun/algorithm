/**
 * @param {character[][]} grid
 * @return {number}
 */

var numIslands = function (grid) {
    for (let col = 0; col < grid.length; col++) {
        for (let row = 0; row < grid[col].length; row++) {
            grid[col][row] = +grid[col][row];
        }
    }

    let color = 2;

    for (let col = 0; col < grid.length; col++) {
        for (let row = 0; row < grid[col].length; row++) {
            if (grid[col][row] === 1) {
                floodFill(grid, col, row, grid.length, grid[col].length, color);
                color++;
            }
        }
    }

    return color - 2;
};

function floodFill(grid, col, row, colMax, rowMax, color) {
    if (col < 0 || row < 0) return;
    else if (col >= colMax || row >= rowMax) return;
    else if (grid[col][row] !== 1) return;

    grid[col][row] = color;
    floodFill(grid, col + 1, row, colMax, rowMax, color);
    floodFill(grid, col - 1, row, colMax, rowMax, color);
    floodFill(grid, col, row + 1, colMax, rowMax, color);
    floodFill(grid, col, row - 1, colMax, rowMax, color);
}
