<h2><a href="https://leetcode.com/problems/split-a-circular-linked-list/">2674. Split a Circular Linked List</a></h2><h3>Medium</h3><hr><div><p>Given a <strong>circular linked list</strong> <code>list</code> of positive integers, your task is to split it into 2 <strong>circular linked lists</strong> so that the first one contains the <strong>first half</strong> of the nodes in <code>list</code> (exactly <code>ceil(list.length / 2)</code> nodes) in the same order they appeared in <code>list</code>, and the second one contains <strong>the rest</strong> of the nodes in <code>list</code> in the same order they appeared in <code>list</code>.</p>

<p>Return <em>an array answer of length 2 in which the first element is a <strong>circular linked list</strong> representing the <strong>first half</strong> and the second element is a <strong>circular linked list</strong> representing the <strong>second half</strong>.</em></p>

<div>A <strong>circular linked list</strong> is a normal linked list with the only difference being that the last node's next node, is the first node.</div>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,5,7]
<strong>Output:</strong> [[1,5],[7]]
<strong>Explanation:</strong> The initial list has 3 nodes so the first half would be the first 2 elements since ceil(3 / 2) = 2 and the rest which is 1 node is in the second half.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [2,6,1,5]
<strong>Output:</strong> [[2,6],[1,5]]
<strong>Explanation:</strong> The initial list has 4 nodes so the first half would be the first 2 elements since ceil(4 / 2) = 2 and the rest which is 2 nodes are in the second half.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in <code>list</code>&nbsp;is in the range <code>[2, 10<sup>5</sup>]</code></li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li><font face="monospace"><code>LastNode.next = FirstNode</code></font> where <code>LastNode</code> is the last node of the list and <code>FirstNode</code> is the first one</li>
</ul>
</div>