<h2> 43 4
2852. Sum of Remoteness of All Cells</h2><hr><div><p>You are given a <strong>0-indexed</strong> matrix <code>grid</code> of order <code>n * n</code>. Each cell in this matrix has a value <code>grid[i][j]</code>, which is either a <strong>positive</strong> integer or <code>-1</code> representing a blocked cell.</p>

<p>You can move from a non-blocked cell to any non-blocked cell that shares an edge.</p>

<p>For any cell <code>(i, j)</code>, we represent its <strong>remoteness</strong> as <code>R[i][j]</code> which is defined as the following:</p>

<ul>
	<li>If the cell <code>(i, j)</code> is a <strong>non-blocked</strong> cell, <code>R[i][j]</code> is the sum of the values <code>grid[x][y]</code> such that there is <strong>no path</strong> from the <strong>non-blocked</strong> cell <code>(x, y)</code> to the cell <code>(i, j)</code>.</li>
	<li>For blocked cells, <code>R[i][j] == 0</code>.</li>
</ul>

<p>Return<em> the sum of </em><code>R[i][j]</code><em> over all cells.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/09/12/1-new.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 400px; height: 304px;"></p>

<pre><strong>Input:</strong> grid = [[-1,1,-1],[5,-1,4],[-1,3,-1]]
<strong>Output:</strong> 39
<strong>Explanation:</strong> In the picture above, there are four grids. The top-left grid contains the initial values in the grid. Blocked cells are colored black, and other cells get their values as it is in the input. In the top-right grid, you can see the value of R[i][j] for all cells. So the answer would be the sum of them. That is: 0 + 12 + 0 + 8 + 0 + 9 + 0 + 10 + 0 = 39.
Let's jump on the bottom-left grid in the above picture and calculate R[0][1] (the target cell is colored green). We should sum up the value of cells that can't be reached by the cell (0, 1). These cells are colored yellow in this grid. So R[0][1] = 5 + 4 + 3 = 12.
Now let's jump on the bottom-right grid in the above picture and calculate R[1][2] (the target cell is colored green). We should sum up the value of cells that can't be reached by the cell (1, 2). These cells are colored yellow in this grid. So R[1][2] = 1 + 5 + 3 = 9.
</pre>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/09/12/2.png" style="width: 400px; height: 302px; background: #fff; border-radius: .5rem;"></p>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> grid = [[-1,3,4],[-1,-1,-1],[3,-1,-1]]
<strong>Output:</strong> 13
<strong>Explanation:</strong> In the picture above, there are four grids. The top-left grid contains the initial values in the grid. Blocked cells are colored black, and other cells get their values as it is in the input. In the top-right grid, you can see the value of R[i][j] for all cells. So the answer would be the sum of them. That is: 3 + 3 + 0 + 0 + 0 + 0 + 7 + 0 + 0 = 13.
Let's jump on the bottom-left grid in the above picture and calculate R[0][2] (the target cell is colored green). We should sum up the value of cells that can't be reached by the cell (0, 2). This cell is colored yellow in this grid. So R[0][2] = 3.
Now let's jump on the bottom-right grid in the above picture and calculate R[2][0] (the target cell is colored green). We should sum up the value of cells that can't be reached by the cell (2, 0). These cells are colored yellow in this grid. So R[2][0] = 3 + 4 = 7.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> grid = [[1]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since there are no other cells than (0, 0), R[0][0] is equal to 0. So the sum of R[i][j] over all cells would be 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 300</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>6</sup></code> or <code>grid[i][j] == -1</code></li>
</ul>
</div>