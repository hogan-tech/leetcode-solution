<h2> 967 153
1222. Queens That Can Attack the King</h2><hr><div><p>On a <strong>0-indexed</strong> <code>8 x 8</code> chessboard, there can be multiple black queens and one white king.</p>

<p>You are given a 2D integer array <code>queens</code> where <code>queens[i] = [xQueen<sub>i</sub>, yQueen<sub>i</sub>]</code> represents the position of the <code>i<sup>th</sup></code> black queen on the chessboard. You are also given an integer array <code>king</code> of length <code>2</code> where <code>king = [xKing, yKing]</code> represents the position of the white king.</p>

<p>Return <em>the coordinates of the black queens that can directly attack the king</em>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/12/21/chess1.jpg" style="width: 400px; height: 400px;">
<pre><strong>Input:</strong> queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
<strong>Output:</strong> [[0,1],[1,0],[3,3]]
<strong>Explanation:</strong> The diagram above shows the three queens that can directly attack the king and the three queens that cannot attack the king (i.e., marked with red dashes).
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/12/21/chess2.jpg" style="width: 400px; height: 400px;">
<pre><strong>Input:</strong> queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
<strong>Output:</strong> [[2,2],[3,4],[4,4]]
<strong>Explanation:</strong> The diagram above shows the three queens that can directly attack the king and the three queens that cannot attack the king (i.e., marked with red dashes).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= queens.length &lt; 64</code></li>
	<li><code>queens[i].length == king.length == 2</code></li>
	<li><code>0 &lt;= xQueen<sub>i</sub>, yQueen<sub>i</sub>, xKing, yKing &lt; 8</code></li>
	<li>All the given positions are <strong>unique</strong>.</li>
</ul>
</div>