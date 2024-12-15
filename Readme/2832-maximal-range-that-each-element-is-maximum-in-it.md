<h2><a href="https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/">2832. Maximal Range That Each Element Is Maximum in It</a></h2><h3>Medium</h3><hr><div><p>You are given a <strong>0-indexed</strong> array <code>nums</code> of <b>distinct </b>integers.</p>

<p>Let us define a <strong>0-indexed </strong>array <code>ans</code> of the same length as <code>nums</code> in the following way:</p>

<ul>
	<li><code>ans[i]</code> is the <strong>maximum</strong> length of a subarray <code>nums[l..r]</code>, such that the maximum element in that subarray is equal to <code>nums[i]</code>.</li>
</ul>

<p>Return<em> the array </em><code>ans</code>.</p>

<p><strong>Note</strong> that a <strong>subarray</strong> is a contiguous part of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,5,4,3,6]
<strong>Output:</strong> [1,4,2,1,5]
<strong>Explanation:</strong> For nums[0] the longest subarray in which 1 is the maximum is nums[0..0] so ans[0] = 1.
For nums[1] the longest subarray in which 5 is the maximum is nums[0..3] so ans[1] = 4.
For nums[2] the longest subarray in which 4 is the maximum is nums[2..3] so ans[2] = 2.
For nums[3] the longest subarray in which 3 is the maximum is nums[3..3] so ans[3] = 1.
For nums[4] the longest subarray in which 6 is the maximum is nums[0..4] so ans[4] = 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> [1,2,3,4,5]
<strong>Explanation:</strong> For nums[i] the longest subarray in which it's the maximum is nums[0..i] so ans[i] = i + 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li>All elements in <code>nums</code> are distinct.</li>
</ul>
</div>