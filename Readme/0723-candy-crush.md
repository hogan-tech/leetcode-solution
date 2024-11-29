<h2><a href="https://leetcode.com/problems/candy-crush/">723. Candy Crush</a></h2><h3>Medium</h3><hr><div><p>This question is about implementing a basic elimination algorithm for Candy Crush.</p>

<p>Given an <code>m x n</code> integer array <code>board</code> representing the grid of candy where <code>board[i][j]</code> represents the type of candy. A value of <code>board[i][j] == 0</code> represents that the cell is empty.</p>

<p>The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:</p>

<ul>
	<li>If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.</li>
	<li>After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.</li>
	<li>After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.</li>
	<li>If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.</li>
</ul>

<p>You need to perform the above rules until the board becomes stable, then return <em>the stable board</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/12/candy_crush_example_2.png" style="width: 600px; height: 411px;">
<pre><strong>Input:</strong> board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
<strong>Output:</strong> [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
<strong>Output:</strong> [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>3 &lt;= m, n &lt;= 50</code></li>
	<li><code>1 &lt;= board[i][j] &lt;= 2000</code></li>
</ul>
</div>