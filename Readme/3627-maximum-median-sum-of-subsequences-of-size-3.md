<h2><a href="https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3">3766. Maximum Median Sum of Subsequences of Size 3</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code> with a length divisible by 3.</p>

<p>You want to make the array empty in steps. In each step, you can select any three elements from the array, compute their <strong>median</strong>, and remove the selected elements from the array.</p>

<p>The <strong>median</strong> of an odd-length sequence is defined as the middle element of the sequence when it is sorted in non-decreasing order.</p>

<p>Return the <strong>maximum</strong> possible sum of the medians computed from the selected elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1,3,2,1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>In the first step, select elements at indices 2, 4, and 5, which have a median 3. After removing these elements, <code>nums</code> becomes <code>[2, 1, 2]</code>.</li>
	<li>In the second step, select elements at indices 0, 1, and 2, which have a median 2. After removing these elements, <code>nums</code> becomes empty.</li>
</ul>

<p>Hence, the sum of the medians is <code>3 + 2 = 5</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,10,10,10,10]</span></p>

<p><strong>Output:</strong> <span class="example-io">20</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>In the first step, select elements at indices 0, 2, and 3, which have a median 10. After removing these elements, <code>nums</code> becomes <code>[1, 10, 10]</code>.</li>
	<li>In the second step, select elements at indices 0, 1, and 2, which have a median 10. After removing these elements, <code>nums</code> becomes empty.</li>
</ul>

<p>Hence, the sum of the medians is <code>10 + 10 = 20</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>nums.length % 3 == 0</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
