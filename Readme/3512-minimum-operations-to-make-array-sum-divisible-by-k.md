<h2><a href="https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k">3846. Minimum Operations to Make Array Sum Divisible by K</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code> and an integer <code>k</code>. You can perform the following operation any number of times:</p>

<ul>
	<li>Select an index <code>i</code> and replace <code>nums[i]</code> with <code>nums[i] - 1</code>.</li>
</ul>

<p>Return the <strong>minimum</strong> number of operations required to make the sum of the array divisible by <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,9,7], k = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Perform 4 operations on <code>nums[1] = 9</code>. Now, <code>nums = [3, 5, 7]</code>.</li>
	<li>The sum is 15, which is divisible by 5.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,1,3], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The sum is 8, which is already divisible by 4. Hence, no operations are needed.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,2], k = 6</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Perform 3 operations on <code>nums[0] = 3</code> and 2 operations on <code>nums[1] = 2</code>. Now, <code>nums = [0, 0]</code>.</li>
	<li>The sum is 0, which is divisible by 6.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>
