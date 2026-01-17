<h2><a href="https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles">3325. Find the Largest Area of Square Inside Two Rectangles</a></h2><h3>Medium</h3><hr><p>There exist <code>n</code> rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays&nbsp;<code>bottomLeft</code> and <code>topRight</code>&nbsp;where <code>bottomLeft[i] = [a_i, b_i]</code> and <code>topRight[i] = [c_i, d_i]</code> represent&nbsp;the <strong>bottom-left</strong> and <strong>top-right</strong> coordinates of the <code>i<sup>th</sup></code> rectangle, respectively.</p>

<p>You need to find the <strong>maximum</strong> area of a <strong>square</strong> that can fit inside the intersecting region of at least two rectangles. Return <code>0</code> if such a square does not exist.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/05/example12.png" style="width: 443px; height: 364px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem;" />
<p><strong>Input:</strong> bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]</p>

<p><strong>Output:</strong> 1</p>

<p><strong>Explanation:</strong></p>

<p>A square with side length 1 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 1. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.</p>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/07/15/diag.png" style="width: 451px; height: 470px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem;" />
<p><strong>Input:</strong> bottomLeft = [[1,1],[1,3],[1,5]], topRight = [[5,5],[5,7],[5,9]]</p>

<p><strong>Output:</strong> 4</p>

<p><strong>Explanation:</strong></p>

<p>A square with side length 2 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is <code>2 * 2 = 4</code>. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.</p>

<p><strong class="example">Example 3:</strong></p>
<code> <img alt="" src="https://assets.leetcode.com/uploads/2024/01/04/rectanglesexample2.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 445px; height: 365px;" /> </code>

<p><strong>Input:</strong> bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]]</p>

<p><strong>Output:</strong> 1</p>

<p><strong>Explanation:</strong></p>

<p>A square with side length 1 can fit inside the intersecting region of any two rectangles. Also, no larger square can, so the maximum area is 1. Note that the region can be formed by the intersection of more than 2 rectangles.</p>

<p><strong class="example">Example 4:</strong></p>
<code> <img alt="" src="https://assets.leetcode.com/uploads/2024/01/04/rectanglesexample3.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 444px; height: 364px;" /> </code>

<p><strong>Input:&nbsp;</strong>bottomLeft = [[1,1],[3,3],[3,1]], topRight = [[2,2],[4,4],[4,2]]</p>

<p><strong>Output:</strong> 0</p>

<p><strong>Explanation:</strong></p>

<p>No pair of rectangles intersect, hence, the answer is 0.</p>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == bottomLeft.length == topRight.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>3</sup></code></li>
	<li><code>bottomLeft[i].length == topRight[i].length == 2</code></li>
	<li><code>1 &lt;= bottomLeft[i][0], bottomLeft[i][1] &lt;= 10<sup>7</sup></code></li>
	<li><code>1 &lt;= topRight[i][0], topRight[i][1] &lt;= 10<sup>7</sup></code></li>
	<li><code>bottomLeft[i][0] &lt; topRight[i][0]</code></li>
	<li><code>bottomLeft[i][1] &lt; topRight[i][1]</code></li>
</ul>
