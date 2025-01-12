<h2> 2 0
3417. Zigzag Grid Traversal With Skip</h2><hr><div><p>You are given an <code>m x n</code> 2D array <code>grid</code> of <strong>positive</strong> integers.</p>

<p>Your task is to traverse <code>grid</code> in a <strong>zigzag</strong> pattern while skipping every <strong>alternate</strong> cell.</p>

<p>Zigzag pattern traversal is defined as following the below actions:</p>

<ul>
	<li>Start at the top-left cell <code>(0, 0)</code>.</li>
	<li>Move <em>right</em> within a row until the end of the row is reached.</li>
	<li>Drop down to the next row, then traverse <em>left</em> until the beginning of the row is reached.</li>
	<li>Continue <strong>alternating</strong> between right and left traversal until every row has been traversed.</li>
</ul>

<p><strong>Note </strong>that you <strong>must skip</strong> every <em>alternate</em> cell during the traversal.</p>

<p>Return an array of integers <code>result</code> containing, <strong>in order</strong>, the value of the cells visited during the zigzag traversal with skips.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,2],[3,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,4]</span></p>

<p><strong>Explanation:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/11/23/4012_example0.png" style="width: 200px; height: 200px;"></strong></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[2,1],[2,1],[2,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,1,2]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/11/23/4012_example1.png" style="width: 200px; height: 240px;"></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,2,3],[4,5,6],[7,8,9]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,3,5,7,9]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/11/23/4012_example2.png" style="width: 260px; height: 250px;"></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n == grid.length &lt;= 50</code></li>
	<li><code>2 &lt;= m == grid[i].length &lt;= 50</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 2500</code></li>
</ul>
</div>