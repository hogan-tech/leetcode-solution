<h2><a href="https://leetcode.com/problems/equal-tree-partition">663. Equal Tree Partition</a></h2><h3>Medium</h3><hr><p>Given the <code>root</code> of a binary tree, return <code>true</code><em> if you can partition the tree into two trees with equal sums of values after removing exactly one edge on the original tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/split1-tree.jpg" style="width: 500px; height: 204px;" />
<pre>
<strong>Input:</strong> root = [5,10,10,null,null,2,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/split2-tree.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [1,2,10,null,null,2,20]
<strong>Output:</strong> false
<strong>Explanation:</strong> You cannot split the tree into two trees with equal sums after removing exactly one edge on the tree.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>
