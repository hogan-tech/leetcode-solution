<h2><a href="https://leetcode.com/problems/bomb-enemy">361. Bomb Enemy</a></h2><h3>Medium</h3><hr><p>Given an <code>m x n</code> matrix <code>grid</code> where each cell is either a wall <code>&#39;W&#39;</code>, an enemy <code>&#39;E&#39;</code> or empty <code>&#39;0&#39;</code>, return <em>the maximum enemies you can kill using one bomb</em>. You can only place the bomb in an empty cell.</p>

<p>The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/27/bomb1-grid.jpg" style="width: 600px; height: 187px;" />
<pre>
<strong>Input:</strong> grid = [[&quot;0&quot;,&quot;E&quot;,&quot;0&quot;,&quot;0&quot;],[&quot;E&quot;,&quot;0&quot;,&quot;W&quot;,&quot;E&quot;],[&quot;0&quot;,&quot;E&quot;,&quot;0&quot;,&quot;0&quot;]]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/27/bomb2-grid.jpg" style="width: 500px; height: 194px;" />
<pre>
<strong>Input:</strong> grid = [[&quot;W&quot;,&quot;W&quot;,&quot;W&quot;],[&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],[&quot;E&quot;,&quot;E&quot;,&quot;E&quot;]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>grid[i][j]</code> is either <code>&#39;W&#39;</code>, <code>&#39;E&#39;</code>, or <code>&#39;0&#39;</code>.</li>
</ul>
