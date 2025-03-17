<h2> 2787 76
1315. Sum of Nodes with Even-Valued Grandparent</h2><hr><div><p>Given the <code>root</code> of a binary tree, return <em>the sum of values of nodes with an <strong>even-valued grandparent</strong></em>. If there are no nodes with an <strong>even-valued grandparent</strong>, return <code>0</code>.</p>

<p>A <strong>grandparent</strong> of a node is the parent of its parent if it exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/10/even1-tree.jpg" style="width: 504px; height: 302px;">
<pre><strong>Input:</strong> root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
<strong>Output:</strong> 18
<strong>Explanation:</strong> The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/10/even2-tree.jpg" style="width: 64px; height: 65px;">
<pre><strong>Input:</strong> root = [1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 100</code></li>
</ul>
</div>