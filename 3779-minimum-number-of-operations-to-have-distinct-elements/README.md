<h2><a href="https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements">4162. Minimum Number of Operations to Have Distinct Elements</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code>.</p>

<p>In one operation, you remove the <strong>first three elements</strong> of the current array. If there are fewer than three elements remaining, <strong>all</strong> remaining elements are removed.</p>

<p>Repeat this operation until the array is empty or contains no duplicate values.</p>

<p>Return an integer denoting the number of operations required.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,8,3,6,5,8]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>In the first operation, we remove the first three elements. The remaining elements <code>[6, 5, 8]</code> are all distinct, so we stop. Only one operation is needed.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>After one operation, the array becomes empty, which meets the stopping condition.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,3,5,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>All elements in the array are distinct, therefore no operations are needed.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
