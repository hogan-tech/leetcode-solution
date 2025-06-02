<h2><a href="https://leetcode.com/problems/partition-array-into-two-equal-product-subsets">3843. Partition Array into Two Equal Product Subsets</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code> containing <strong>distinct</strong> positive integers and an integer <code>target</code>.</p>

<p>Determine if you can partition <code>nums</code> into two <strong>non-empty</strong> <strong>disjoint</strong> <strong>subsets</strong>, with each element belonging to <strong>exactly one</strong> subset, such that the product of the elements in each subset is equal to <code>target</code>.</p>

<p>Return <code>true</code> if such a partition exists and <code>false</code> otherwise.</p>
A <strong>subset</strong> of an array is a selection of elements of the array.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,1,6,8,4], target = 24</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong> The subsets <code>[3, 8]</code> and <code>[1, 6, 4]</code> each have a product of 24. Hence, the output is true.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,5,3,7], target = 15</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong> There is no way to partition <code>nums</code> into two non-empty disjoint subsets such that both subsets have a product of 15. Hence, the output is false.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 12</code></li>
	<li><code>1 &lt;= target &lt;= 10<sup>15</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li>All elements of <code>nums</code> are <strong>distinct</strong>.</li>
</ul>
