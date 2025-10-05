<h2><a href="https://leetcode.com/problems/compute-alternating-sum">4058. Compute Alternating Sum</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code>.</p>

<p>The <strong>alternating sum</strong> of <code>nums</code> is the value obtained by <strong>adding</strong> elements at even indices and <strong>subtracting</strong> elements at odd indices. That is, <code>nums[0] - nums[1] + nums[2] - nums[3]...</code></p>

<p>Return an integer denoting the alternating sum of <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3,5,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">-4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Elements at even indices are <code>nums[0] = 1</code> and <code>nums[2] = 5</code> because 0 and 2 are even numbers.</li>
	<li>Elements at odd indices are <code>nums[1] = 3</code> and <code>nums[3] = 7</code> because 1 and 3 are odd numbers.</li>
	<li>The alternating sum is <code>nums[0] - nums[1] + nums[2] - nums[3] = 1 - 3 + 5 - 7 = -4</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [100]</span></p>

<p><strong>Output:</strong> <span class="example-io">100</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The only element at even indices is <code>nums[0] = 100</code> because 0 is an even number.</li>
	<li>There are no elements on odd indices.</li>
	<li>The alternating sum is <code>nums[0] = 100</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>
