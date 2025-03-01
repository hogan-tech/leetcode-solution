<h2> 8 0
3467. Transform Array by Parity</h2><hr><div><p>You are given an integer array <code>nums</code>. Transform <code>nums</code> by performing the following operations in the <strong>exact</strong> order specified:</p>

<ol>
	<li>Replace each even number with 0.</li>
	<li>Replace each odd numbers with 1.</li>
	<li>Sort the modified array in <strong>non-decreasing</strong> order.</li>
</ol>

<p>Return the resulting array after performing these operations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,3,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,0,1,1]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with 1. Now, <code>nums = [0, 1, 0, 1]</code>.</li>
	<li>After sorting <code>nums</code> in non-descending order, <code>nums = [0, 0, 1, 1]</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,5,1,4,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,0,1,1,1]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Replace the even numbers (4 and 2) with 0 and the odd numbers (1, 5 and 1) with 1. Now, <code>nums = [1, 1, 1, 0, 0]</code>.</li>
	<li>After sorting <code>nums</code> in non-descending order, <code>nums = [0, 0, 1, 1, 1]</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>
</div>