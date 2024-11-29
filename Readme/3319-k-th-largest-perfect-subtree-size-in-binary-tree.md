<h2><a href="https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/">3319. K-th Largest Perfect Subtree Size in Binary Tree</a></h2><h3>Medium</h3><hr><div><p>You are given the <code>root</code> of a <strong>binary tree</strong> and an integer <code>k</code>.</p>

<p>Return an integer denoting the size of the <code>k<sup>th</sup></code> <strong>largest<em> </em>perfect binary</strong><em> </em><span data-keyword="subtree">subtree</span>, or <code>-1</code> if it doesn't exist.</p>

<p>A <strong>perfect binary tree</strong> is a tree where all leaves are on the same level, and every parent has two children.</p>

<p>A <strong>subtree</strong> of <code>treeName</code> is a tree consisting of a node in <code>treeName</code> and all of its descendants.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [5,3,6,5,2,5,7,1,8,null,null,6,8], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/21/image.jpg" style="width: 300px; height: 175px;"></p>

<p>The roots of the perfect binary subtrees are highlighted in black. Their sizes, in decreasing order are <code>[3, 3, 1, 1, 1, 1, 1, 1]</code>.<br>
The <code>2<sup>nd</sup></code> largest size is 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [1,2,3,4,5,6,7], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/21/image1.jpg" style="width: 300px; height: 149px;"></p>

<p>The sizes of the perfect binary subtrees in decreasing order are <code>[7, 3, 3, 1, 1, 1, 1]</code>. The size of the largest perfect binary subtree is 7.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">root = [1,2,3,null,4], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/21/image4.jpg" style="width: 150px; height: 130px;"></p>

<p>The sizes of the perfect binary subtrees in decreasing order are <code>[1, 1]</code>. There are fewer than 3 perfect binary subtrees.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 2000]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 2000</code></li>
	<li><code>1 &lt;= k &lt;= 1024</code></li>
</ul>
</div>