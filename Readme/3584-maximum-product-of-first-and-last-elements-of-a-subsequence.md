<h2><a href="https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence">3755. Maximum Product of First and Last Elements of a Subsequence</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code> and an integer <code>m</code>.</p>

<p>Return the <strong>maximum</strong> product of the first and last elements of any <strong><span data-keyword="subsequence-array">subsequence</span></strong> of <code>nums</code> of size <code>m</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-1,-9,2,3,-2,-3,1], m = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">81</span></p>

<p><strong>Explanation:</strong></p>

<p>The subsequence <code>[-9]</code> has the largest product of the first and last elements: <code>-9 * -9 = 81</code>. Therefore, the answer is 81.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3,-5,5,6,-4], m = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">20</span></p>

<p><strong>Explanation:</strong></p>

<p>The subsequence <code>[-5, 6, -4]</code> has the largest product of the first and last elements.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,-1,2,-6,5,2,-5,7], m = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">35</span></p>

<p><strong>Explanation:</strong></p>

<p>The subsequence <code>[5, 7]</code> has the largest product of the first and last elements.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m &lt;= nums.length</code></li>
</ul>
