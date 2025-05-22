<h2><a href="https://leetcode.com/problems/valid-tic-tac-toe-state">810. Valid Tic-Tac-Toe State</a></h2><h3>Medium</h3><hr><p>Given a Tic-Tac-Toe board as a string array <code>board</code>, return <code>true</code> if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.</p>

<p>The board is a <code>3 x 3</code> array that consists of characters <code>&#39; &#39;</code>, <code>&#39;X&#39;</code>, and <code>&#39;O&#39;</code>. The <code>&#39; &#39;</code> character represents an empty square.</p>

<p>Here are the rules of Tic-Tac-Toe:</p>

<ul>
	<li>Players take turns placing characters into empty squares <code>&#39; &#39;</code>.</li>
	<li>The first player always places <code>&#39;X&#39;</code> characters, while the second player always places <code>&#39;O&#39;</code> characters.</li>
	<li><code>&#39;X&#39;</code> and <code>&#39;O&#39;</code> characters are always placed into empty squares, never filled ones.</li>
	<li>The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.</li>
	<li>The game also ends if all squares are non-empty.</li>
	<li>No more moves can be played if the game is over.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/15/tictactoe1-grid.jpg" style="width: 253px; height: 253px;" />
<pre>
<strong>Input:</strong> board = [&quot;O  &quot;,&quot;   &quot;,&quot;   &quot;]
<strong>Output:</strong> false
<strong>Explanation:</strong> The first player always plays &quot;X&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/15/tictactoe2-grid.jpg" style="width: 253px; height: 253px;" />
<pre>
<strong>Input:</strong> board = [&quot;XOX&quot;,&quot; X &quot;,&quot;   &quot;]
<strong>Output:</strong> false
<strong>Explanation:</strong> Players take turns making moves.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/15/tictactoe4-grid.jpg" style="width: 253px; height: 253px;" />
<pre>
<strong>Input:</strong> board = [&quot;XOX&quot;,&quot;O O&quot;,&quot;XOX&quot;]
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>board.length == 3</code></li>
	<li><code>board[i].length == 3</code></li>
	<li><code>board[i][j]</code> is either <code>&#39;X&#39;</code>, <code>&#39;O&#39;</code>, or <code>&#39; &#39;</code>.</li>
</ul>
