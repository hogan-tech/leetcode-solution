<h2><a href="https://leetcode.com/problems/partition-array-into-k-distinct-groups">3979. Partition Array Into K-Distinct Groups</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>Your task is to determine whether it is possible to partition all elements of <code>nums</code> into one or more groups such that:</p>

<ul>
	<li>Each group contains <strong>exactly</strong> <code>k</code> elements.</li>
	<li>All elements in each group are <strong>distinct</strong>.</li>
	<li>Each element in <code>nums</code> must be assigned to <strong>exactly</strong> one group.</li>
</ul>

<p>Return <code>true</code> if such a partition is possible, otherwise return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>One possible partition is to have 2 groups:</p>

<ul>
	<li>Group 1: <code>[1, 2]</code></li>
	<li>Group 2: <code>[3, 4]</code></li>
</ul>

<p>Each group contains <code>k = 2</code> distinct elements, and all elements are used exactly once.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,5,2,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>One possible partition is to have 2 groups:</p>

<ul>
	<li>Group 1: <code>[2, 3]</code></li>
	<li>Group 2: <code>[2, 5]</code></li>
</ul>

<p>Each group contains <code>k = 2</code> distinct elements, and all elements are used exactly once.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,5,2,3], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>We cannot form groups of <code>k = 3</code> distinct elements using all values exactly once.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code><sup>​​​​​​​</sup>1 &lt;= k &lt;= nums.length</code></li>
</ul>
