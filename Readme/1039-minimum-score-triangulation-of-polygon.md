<h2><a href="https://leetcode.com/problems/minimum-score-triangulation-of-polygon">1111. Minimum Score Triangulation of Polygon</a></h2><h3>Medium</h3><hr><p>You have a convex <code>n</code>-sided polygon where each vertex has an integer value. You are given an integer array <code>values</code> where <code>values[i]</code> is the value of the <code>i<sup>th</sup></code> vertex in <strong>clockwise order</strong>.</p>

<p><strong>Polygon</strong> <strong>triangulation</strong> is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in <code>n - 2</code> triangles.</p>

<p>You will <strong>triangulate</strong> the polygon. For each triangle, the <em>weight</em> of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these <em>weights</em> over all <code>n - 2</code> triangles.</p>

<p>Return the<em> minimum possible score </em>that you can achieve with some<em> </em><strong>triangulation</strong><em> </em>of the polygon.</p>


<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="http://127.0.0.1:49174/shape1.jpg" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">values = [1,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong> The polygon is already triangulated, and the score of the only triangle is 6.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="http://127.0.0.1:49174/shape2.jpg" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">values = [3,7,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">144</span></p>

<p><strong>Explanation:</strong> There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.<br />
The minimum score is 144.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<p><img alt="" src="http://127.0.0.1:49174/shape3.jpg" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">values = [1,3,1,4,1,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">13</span></p>

<p><strong>Explanation:</strong> The minimum score triangulation is 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == values.length</code></li>
	<li><code>3 &lt;= n &lt;= 50</code></li>
	<li><code>1 &lt;= values[i] &lt;= 100</code></li>
</ul>
