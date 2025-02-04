<h2> 466 65
2428. Maximum Sum of an Hourglass</h2><hr><div><p>You are given an <code>m x n</code> integer matrix <code>grid</code>.</p>

<p>We define an <strong>hourglass</strong> as a part of the matrix with the following form:</p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/08/21/img.jpg" style="width: 243px; height: 243px;">
<p>Return <em>the <strong>maximum</strong> sum of the elements of an hourglass</em>.</p>

<p><strong>Note</strong> that an hourglass cannot be rotated and must be entirely contained within the matrix.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/08/21/1.jpg" style="width: 323px; height: 323px;">
<pre><strong>Input:</strong> grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
<strong>Output:</strong> 30
<strong>Explanation:</strong> The cells shown above represent the hourglass with the maximum sum: 6 + 2 + 1 + 2 + 9 + 2 + 8 = 30.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/08/21/2.jpg" style="width: 243px; height: 243px;">
<pre><strong>Input:</strong> grid = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> 35
<strong>Explanation:</strong> There is only one hourglass in the matrix, with the sum: 1 + 2 + 3 + 5 + 7 + 8 + 9 = 35.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>3 &lt;= m, n &lt;= 150</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>6</sup></code></li>
</ul>
</div>