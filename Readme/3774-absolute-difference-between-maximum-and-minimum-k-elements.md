<h2><a href="https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements">4158. Absolute Difference Between Maximum and Minimum K Elements</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>Find the absolute difference between:</p>

<ul>
	<li>the <strong>sum</strong> of the <code>k</code> <strong>largest</strong> elements in the array; and</li>
	<li>the <strong>sum</strong> of the <code>k</code> <strong>smallest</strong> elements in the array.</li>
</ul>

<p>Return an integer denoting this difference.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,2,2,4], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The <code>k = 2</code> largest elements are 4 and 5. Their sum is <code>4 + 5 = 9</code>.</li>
	<li>The <code>k = 2</code> smallest elements are 2 and 2. Their sum is <code>2 + 2 = 4</code>.</li>
	<li>The absolute difference is <code>abs(9 - 4) = 5</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [100], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The largest element is 100.</li>
	<li>The smallest element is 100.</li>
	<li>The absolute difference is <code>abs(100 - 100) = 0</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>
