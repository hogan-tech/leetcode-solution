<h2> 129 209
2711. Difference of Number of Distinct Values on Diagonals</h2><hr><div><p>Given a 2D <code>grid</code> of size <code>m x n</code>, you should find the matrix <code>answer</code> of size <code>m x n</code>.</p>

<p>The cell <code>answer[r][c]</code> is calculated by looking at the diagonal values of the cell <code>grid[r][c]</code>:</p>

<ul>
	<li>Let <code>leftAbove[r][c]</code> be the number of <strong>distinct</strong> values on the diagonal to the left and above the cell <code>grid[r][c]</code> not including the cell <code>grid[r][c]</code> itself.</li>
	<li>Let <code>rightBelow[r][c]</code> be the number of <strong>distinct</strong> values on the diagonal to the right and below the cell <code>grid[r][c]</code>, not including the cell <code>grid[r][c]</code> itself.</li>
	<li>Then <code>answer[r][c] = |leftAbove[r][c] - rightBelow[r][c]|</code>.</li>
</ul>

<p>A <strong>matrix diagonal</strong> is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until the end of the matrix is reached.</p>

<ul>
	<li>For example, in the below diagram the diagonal is highlighted using the cell with indices <code>(2, 3)</code> colored gray:

	<ul>
		<li>Red-colored cells are left and above the cell.</li>
		<li>Blue-colored cells are right and below the cell.</li>
	</ul>
	</li>
</ul>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/26/diagonal.png" style="width: 200px; height: 160px;"></p>

<p>Return the matrix <code>answer</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,2,3],[3,1,5],[3,2,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">Output: [[1,1,0],[1,0,1],[0,1,1]]</span></p>

<p><strong>Explanation:</strong></p>

<p>To calculate the <code>answer</code> cells:</p>

<table>
	<thead>
		<tr>
			<th>answer</th>
			<th>left-above elements</th>
			<th>leftAbove</th>
			<th>right-below elements</th>
			<th>rightBelow</th>
			<th>|leftAbove - rightBelow|</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>[0][0]</td>
			<td>[]</td>
			<td>0</td>
			<td>[grid[1][1], grid[2][2]]</td>
			<td>|{1, 1}| = 1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>[0][1]</td>
			<td>[]</td>
			<td>0</td>
			<td>[grid[1][2]]</td>
			<td>|{5}| = 1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>[0][2]</td>
			<td>[]</td>
			<td>0</td>
			<td>[]</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td>[1][0]</td>
			<td>[]</td>
			<td>0</td>
			<td>[grid[2][1]]</td>
			<td>|{2}| = 1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>[1][1]</td>
			<td>[grid[0][0]]</td>
			<td>|{1}| = 1</td>
			<td>[grid[2][2]]</td>
			<td>|{1}| = 1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>[1][2]</td>
			<td>[grid[0][1]]</td>
			<td>|{2}| = 1</td>
			<td>[]</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>[2][0]</td>
			<td>[]</td>
			<td>0</td>
			<td>[]</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td>[2][1]</td>
			<td>[grid[1][0]]</td>
			<td>|{3}| = 1</td>
			<td>[]</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>[2][2]</td>
			<td>[grid[0][0], grid[1][1]]</td>
			<td>|{1, 1}| = 1</td>
			<td>[]</td>
			<td>0</td>
			<td>1</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">Output: [[0]]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n, grid[i][j] &lt;= 50</code></li>
</ul>
</div>