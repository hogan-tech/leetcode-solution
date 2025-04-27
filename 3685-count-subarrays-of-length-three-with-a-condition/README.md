<h2><a href="https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition">3685. Count Subarrays of Length Three With a Condition</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code>, return the number of <span data-keyword="subarray-nonempty">subarrays</span> of length 3 such that the sum of the first and third numbers equals <em>exactly</em> half of the second number.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1,4,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Only the subarray <code>[1,4,1]</code> contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p><code>[1,1,1]</code> is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 100</code></li>
	<li><code><font face="monospace">-100 &lt;= nums[i] &lt;= 100</font></code></li>
</ul>
