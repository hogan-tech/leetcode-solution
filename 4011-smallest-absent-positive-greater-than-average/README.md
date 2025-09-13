<h2><a href="https://leetcode.com/problems/smallest-absent-positive-greater-than-average">4011. Smallest Absent Positive Greater Than Average</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code>.</p>

<p>Return the <strong>smallest absent positive</strong> integer in <code>nums</code> such that it is <strong>strictly greater</strong> than the <strong>average</strong> of all elements in <code>nums</code>.</p>
The <strong>average</strong> of an array is defined as the sum of all its elements divided by the number of elements.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The average of <code>nums</code> is <code>(3 + 5) / 2 = 8 / 2 = 4</code>.</li>
	<li>The smallest absent positive integer greater than 4 is 6.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-1,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>​​​​​​​The average of <code>nums</code> is <code>(-1 + 1 + 2) / 3 = 2 / 3 = 0.667</code>.</li>
	<li>The smallest absent positive integer greater than 0.667 is 3.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,-1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The average of <code>nums</code> is <code>(4 + (-1)) / 2 = 3 / 2 = 1.50</code>.</li>
	<li>The smallest absent positive integer greater than 1.50 is 2.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code>​​​​​​​</li>
</ul>
