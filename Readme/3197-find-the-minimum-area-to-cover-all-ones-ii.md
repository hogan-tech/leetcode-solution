<h2><a href="https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii">3459. Find the Minimum Area to Cover All Ones II</a></h2><h3>Hard</h3><hr><p>You are given a 2D <strong>binary</strong> array <code>grid</code>. You need to find 3 <strong>non-overlapping</strong> rectangles having <strong>non-zero</strong> areas with horizontal and vertical sides such that all the 1&#39;s in <code>grid</code> lie inside these rectangles.</p>

<p>Return the <strong>minimum</strong> possible sum of the area of these rectangles.</p>

<p><strong>Note</strong> that the rectangles are allowed to touch.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,0,1],[1,1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/14/example0rect21.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 280px; height: 198px;" /></p>

<ul>
	<li>The 1&#39;s at <code>(0, 0)</code> and <code>(1, 0)</code> are covered by a rectangle of area 2.</li>
	<li>The 1&#39;s at <code>(0, 2)</code> and <code>(1, 2)</code> are covered by a rectangle of area 2.</li>
	<li>The 1 at <code>(1, 1)</code> is covered by a rectangle of area 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,0,1,0],[0,1,0,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/14/example1rect2.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 356px; height: 198px;" /></p>

<ul>
	<li>The 1&#39;s at <code>(0, 0)</code> and <code>(0, 2)</code> are covered by a rectangle of area 3.</li>
	<li>The 1 at <code>(1, 1)</code> is covered by a rectangle of area 1.</li>
	<li>The 1 at <code>(1, 3)</code> is covered by a rectangle of area 1.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[i].length &lt;= 30</code></li>
	<li><code>grid[i][j]</code> is either 0 or 1.</li>
	<li>The input is generated such that there are at least three 1&#39;s in <code>grid</code>.</li>
</ul>
