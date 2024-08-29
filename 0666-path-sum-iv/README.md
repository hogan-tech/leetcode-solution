<h2><a href="https://leetcode.com/problems/path-sum-iv/">666. Path Sum IV</a></h2><h3>Medium</h3><hr><div><p>If the depth of a tree is smaller than <code>5</code>, then this tree can be represented by an array of three-digit integers. For each integer in this array:</p>

<ul>
	<li>The hundreds digit represents the depth <code>d</code> of this node where <code>1 &lt;= d &lt;= 4</code>.</li>
	<li>The tens digit represents the position <code>p</code> of this node in the level it belongs to where <code>1 &lt;= p &lt;= 8</code>. The position is the same as that in a full binary tree.</li>
	<li>The units digit represents the value <code>v</code> of this node where <code>0 &lt;= v &lt;= 9</code>.</li>
</ul>

<p>Given an array of <strong>ascending</strong> three-digit integers <code>nums</code> representing a binary tree with a depth smaller than <code>5</code>, return <em>the sum of all paths from the root towards the leaves</em>.</p>

<p>It is <strong>guaranteed</strong> that the given array represents a valid connected binary tree.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/30/pathsum4-1-tree.jpg" style="width: 212px; height: 183px;">
<pre><strong>Input:</strong> nums = [113,215,221]
<strong>Output:</strong> 12
<strong>Explanation:</strong> The tree that the list represents is shown.
The path sum is (3 + 5) + (3 + 1) = 12.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/30/pathsum4-2-tree.jpg" style="width: 132px; height: 183px;">
<pre><strong>Input:</strong> nums = [113,221]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The tree that the list represents is shown. 
The path sum is (3 + 1) = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 15</code></li>
	<li><code>110 &lt;= nums[i] &lt;= 489</code></li>
	<li><code>nums</code> represents a valid binary tree with depth less than <code>5</code>.</li>
	<li><code>nums</code> is sorted in ascending order.</li>
</ul>
</div>