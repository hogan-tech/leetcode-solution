<h2><a href="https://leetcode.com/problems/binary-tree-longest-consecutive-sequence">298. Binary Tree Longest Consecutive Sequence</a></h2><h3>Medium</h3><hr><p>Given the <code>root</code> of a binary tree, return <em>the length of the longest <strong>consecutive sequence path</strong></em>.</p>

<p>A <strong>consecutive sequence path</strong> is a path where the values <strong>increase by one</strong> along the path.</p>

<p>Note that the path can start <strong>at any node</strong> in the tree, and you cannot go from a node to its parent in the path.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/consec1-1-tree.jpg" style="width: 306px; height: 400px;" />
<pre>
<strong>Input:</strong> root = [1,null,3,2,4,null,null,null,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Longest consecutive sequence path is 3-4-5, so return 3.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/consec1-2-tree.jpg" style="width: 249px; height: 400px;" />
<pre>
<strong>Input:</strong> root = [2,null,3,2,null,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 3 * 10<sup>4</sup>]</code>.</li>
	<li><code>-3 * 10<sup>4</sup> &lt;= Node.val &lt;= 3 * 10<sup>4</sup></code></li>
</ul>
