<h2><a href="https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array">3747. Maximum Difference Between Adjacent Elements in a Circular Array</a></h2><h3>Easy</h3><hr><p>Given a <strong>circular</strong> array <code>nums</code>, find the <b>maximum</b> absolute difference between adjacent elements.</p>

<p><strong>Note</strong>: In a circular array, the first and last elements are adjacent.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>Because <code>nums</code> is circular, <code>nums[0]</code> and <code>nums[2]</code> are adjacent. They have the maximum absolute difference of <code>|4 - 1| = 3</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-5,-10,-5]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The adjacent elements <code>nums[0]</code> and <code>nums[1]</code> have the maximum absolute difference of <code>|-5 - (-10)| = 5</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>
