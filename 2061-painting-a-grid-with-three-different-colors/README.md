<h2><a href="https://leetcode.com/problems/painting-a-grid-with-three-different-colors">2061. Painting a Grid With Three Different Colors</a></h2><h3>Hard</h3><hr><p>You are given two integers <code>m</code> and <code>n</code>. Consider an <code>m x n</code> grid where each cell is initially white. You can paint each cell <strong>red</strong>, <strong>green</strong>, or <strong>blue</strong>. All cells <strong>must</strong> be painted.</p>

<p>Return<em> the number of ways to color the grid with <strong>no two adjacent cells having the same color</strong></em>. Since the answer can be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/22/colorthegrid.png" style="width: 200px; height: 50px;" />
<pre>
<strong>Input:</strong> m = 1, n = 1
<strong>Output:</strong> 3
<strong>Explanation:</strong> The three possible colorings are shown in the image above.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/22/copy-of-colorthegrid.png" style="width: 321px; height: 121px;" />
<pre>
<strong>Input:</strong> m = 1, n = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> The six possible colorings are shown in the image above.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> m = 5, n = 5
<strong>Output:</strong> 580986
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m &lt;= 5</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>
