<h2><a href="https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii">549. Binary Tree Longest Consecutive Sequence II</a></h2><h3>Medium</h3><hr><p>Given the <code>root</code> of a binary tree, return <em>the length of the longest consecutive path in the tree</em>.</p>

<p>A consecutive path is a path where the values of the consecutive nodes in the path differ by one. This path can be either increasing or decreasing.</p>

<ul>
	<li>For example, <code>[1,2,3,4]</code> and <code>[4,3,2,1]</code> are both considered valid, but the path <code>[1,2,4,3]</code> is not valid.</li>
</ul>

<p>On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/consec2-1-tree.jpg" style="width: 207px; height: 183px;" />
<pre>
<strong>Input:</strong> root = [1,2,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest consecutive path is [1, 2] or [2, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/consec2-2-tree.jpg" style="width: 207px; height: 183px;" />
<pre>
<strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest consecutive path is [1, 2, 3] or [3, 2, 1].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 3 * 10<sup>4</sup>]</code>.</li>
	<li><code>-3 * 10<sup>4</sup> &lt;= Node.val &lt;= 3 * 10<sup>4</sup></code></li>
</ul>
