/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    let queue = [];
    let rows = grid.length;
    let cols = grid[0].length;
    let freshOranges = 0;

    // Populate queue with initial rotten oranges and count fresh oranges
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (grid[r][c] === 2) {
                queue.push([r, c]); // Add rotten orange to the queue
            } else if (grid[r][c] === 1) {
                freshOranges += 1; // Count fresh oranges
            }
        }
    }

    queue.push([-1, -1]); // Marker to indicate minute elapsed
    let minutesElapsed = -1;
    const directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]; // Direction vectors for adjacent cells

    // BFS traversal using the queue
    while (queue.length > 0) {
        let [row, col] = queue.shift();
        if (row === -1) {
            // Increment time when marker is encountered
            minutesElapsed += 1;
            if (queue.length > 0) {
                queue.push([-1, -1]); // Add marker back if there are still oranges to process
            }
        } else {
            // Process adjacent cells
            for (let d of directions) {
                let nextRow = row + d[0];
                let nextCol = col + d[1];
                // Check bounds and if adjacent cell contains a fresh orange
                if (nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols && grid[nextRow][nextCol] === 1) {
                    grid[nextRow][nextCol] = 2; // Mark orange as rotten
                    freshOranges -= 1; // Decrease fresh orange count
                    queue.push([nextRow, nextCol]); // Add newly rotten orange to the queue
                }
            }
        }
    }

    // If there are still fresh oranges, return -1, otherwise return the time elapsed
    return freshOranges === 0 ? minutesElapsed : -1;
};

// Example usage
let grid = [[2,1,1],[1,1,0],[0,1,1]];
console.log(orangesRotting(grid)); // Output: 4
