<h2><a href="https://leetcode.com/problems/the-knights-tour/">2664. The Knight’s Tour</a></h2><h3>Medium</h3><hr><div><p>Given two positive integers <code>m</code> and <code>n</code> which are the height and width of a <strong>0-indexed</strong> 2D-array <code>board</code>, a pair of positive integers <code>(r, c)</code> which is the starting position of the knight on the board.</p>

<p>Your task is to find an order of movements for the knight, in a manner that every cell of the&nbsp;<code>board</code> gets visited <strong>exactly</strong> once (the starting cell is considered visited and you <strong>shouldn't</strong> visit it again).</p>

<p>Return <em>the array</em> <code>board</code> <em>in which the cells' values show the order of visiting the cell starting from 0 (the initial place of the knight).</em></p>

<p>Note that a <strong>knight</strong> can <strong>move</strong> from cell <code>(r1, c1)</code> to cell <code>(r2, c2)</code> if <code>0 &lt;= r2 &lt;= m - 1</code> and <code>0 &lt;= c2 &lt;= n - 1</code> and <code>min(abs(r1 - r2), abs(c1 - c2)) = 1</code> and <code>max(abs(r1 - r2), abs(c1 - c2)) = 2</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> m = 1, n = 1, r = 0, c = 0
<strong>Output:</strong> [[0]]
<strong>Explanation:</strong> There is only 1 cell and the knight is initially on it so there is only a 0 inside the 1x1 grid.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> m = 3, n = 4, r = 0, c = 0
<strong>Output:</strong> [[0,3,6,9],[11,8,1,4],[2,5,10,7]]
<strong>Explanation:</strong> By the following order of movements we can visit the entire board.
(0,0)-&gt;(1,2)-&gt;(2,0)-&gt;(0,1)-&gt;(1,3)-&gt;(2,1)-&gt;(0,2)-&gt;(2,3)-&gt;(1,1)-&gt;(0,3)-&gt;(2,2)-&gt;(1,0)</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m,&nbsp;n &lt;= 5</code></li>
	<li><code>0 &lt;= r &lt;= m - 1</code></li>
	<li><code>0 &lt;= c &lt;= n - 1</code></li>
	<li>The inputs will be generated such that there exists at least one&nbsp;possible order of movements with the given condition</li>
</ul>
</div>