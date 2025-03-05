<h2> 917 183
1138. Alphabet Board Path</h2><hr><div><p>On an alphabet board, we start at position <code>(0, 0)</code>, corresponding to character&nbsp;<code>board[0][0]</code>.</p>

<p>Here, <code>board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]</code>, as shown in the diagram below.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/07/28/azboard.png" style="width: 250px; height: 317px;"></p>

<p>We may make the following moves:</p>

<ul>
	<li><code>'U'</code> moves our position up one row, if the position exists on the board;</li>
	<li><code>'D'</code> moves our position down one row, if the position exists on the board;</li>
	<li><code>'L'</code> moves our position left one column, if the position exists on the board;</li>
	<li><code>'R'</code> moves our position right one column, if the position exists on the board;</li>
	<li><code>'!'</code>&nbsp;adds the character <code>board[r][c]</code> at our current position <code>(r, c)</code>&nbsp;to the&nbsp;answer.</li>
</ul>

<p>(Here, the only positions that exist on the board are positions with letters on them.)</p>

<p>Return a sequence of moves that makes our answer equal to <code>target</code>&nbsp;in the minimum number of moves.&nbsp; You may return any path that does so.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> target = "leet"
<strong>Output:</strong> "DDR!UURRR!!DDD!"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> target = "code"
<strong>Output:</strong> "RR!DDRR!UUL!R!"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 100</code></li>
	<li><code>target</code> consists only of English lowercase letters.</li>
</ul></div>