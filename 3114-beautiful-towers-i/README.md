<h2><a href="https://leetcode.com/problems/beautiful-towers-i">3114. Beautiful Towers I</a></h2><h3>Medium</h3><hr><p>You are given an array <code>heights</code> of <code>n</code> integers representing the number of bricks in <code>n</code> consecutive towers. Your task is to remove some bricks to form a <strong>mountain-shaped</strong> tower arrangement. In this arrangement, the tower heights are non-decreasing, reaching a maximum peak value with one or multiple consecutive towers and then non-increasing.</p>

<p>Return the <strong>maximum possible sum</strong> of heights of a mountain-shaped tower arrangement.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">heights = [5,3,4,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">13</span></p>

<p><strong>Explanation:</strong></p>

<p>We remove some bricks to make <code>heights =&nbsp;[5,3,3,1,1]</code>, the peak is at index 0.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">heights = [6,5,3,9,2,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">22</span></p>

<p><strong>Explanation:</strong></p>

<p>We remove some bricks to make <code>heights =&nbsp;[3,3,3,9,2,2]</code>, the peak is at index 3.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">heights = [3,2,5,5,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">18</span></p>

<p><strong>Explanation:</strong></p>

<p>We remove some bricks to make <code>heights = [2,2,5,5,2,2]</code>, the peak is at index 2 or 3.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == heights.length &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= heights[i] &lt;= 10<sup>9</sup></code></li>
</ul>
