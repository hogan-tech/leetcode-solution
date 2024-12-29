<h2> 1 0
3402. Minimum Operations to Make Columns Strictly Increasing</h2><hr><div><p>You are given a <code>m x n</code> matrix <code>grid</code> consisting of <b>non-negative</b> integers.</p>

<p>In one operation, you can increment the value of any <code>grid[i][j]</code> by 1.</p>

<p>Return the <strong>minimum</strong> number of operations needed to make all columns of <code>grid</code> <strong>strictly increasing</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[3,2],[1,3],[3,4],[0,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>To make the <code>0<sup>th</sup></code> column strictly increasing, we can apply 3 operations on <code>grid[1][0]</code>, 2 operations on <code>grid[2][0]</code>, and 6 operations on <code>grid[3][0]</code>.</li>
	<li>To make the <code>1<sup>st</sup></code> column strictly increasing, we can apply 4 operations on <code>grid[3][1]</code>.</li>
</ul>
<img alt="" src="https://assets.leetcode.com/uploads/2024/11/10/firstexample.png" style="width: 200px; height: 347px;"></div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[3,2,1],[2,1,0],[1,2,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>To make the <code>0<sup>th</sup></code> column strictly increasing, we can apply 2 operations on <code>grid[1][0]</code>, and 4 operations on <code>grid[2][0]</code>.</li>
	<li>To make the <code>1<sup>st</sup></code> column strictly increasing, we can apply 2 operations on <code>grid[1][1]</code>, and 2 operations on <code>grid[2][1]</code>.</li>
	<li>To make the <code>2<sup>nd</sup></code> column strictly increasing, we can apply 2 operations on <code>grid[1][2]</code>.</li>
</ul>
<img alt="" src="https://assets.leetcode.com/uploads/2024/11/10/secondexample.png" style="width: 300px; height: 257px;"></div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>0 &lt;= grid[i][j] &lt; 2500</code></li>
</ul>

<p>&nbsp;</p>
<div class="spoiler">
<div>
<pre>
&nbsp;</pre>
</div>
</div>
</div>