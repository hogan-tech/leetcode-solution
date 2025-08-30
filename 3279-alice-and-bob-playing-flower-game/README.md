<h2><a href="https://leetcode.com/problems/alice-and-bob-playing-flower-game">3279. Alice and Bob Playing Flower Game</a></h2><h3>Medium</h3><hr><p>Alice and Bob are playing a turn-based game on a field, with two lanes of flowers between them. There are <code>x</code> flowers in the first lane between Alice and Bob, and <code>y</code> flowers in the second lane between them.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/08/27/3021.png" style="width: 300px; height: 150px;" /></p>

<p>The game proceeds as follows:</p>

<ol>
	<li>Alice takes the first turn.</li>
	<li>In each turn, a player must choose either one of the lane&nbsp;and pick one flower from that side.</li>
	<li>At the end of the turn, if there are no flowers left at all, the <strong>current</strong> player captures their opponent and wins the game.</li>
</ol>

<p>Given two integers, <code>n</code> and <code>m</code>, the task is to compute the number of possible pairs <code>(x, y)</code> that satisfy the conditions:</p>

<ul>
	<li>Alice must win the game according to the described rules.</li>
	<li>The number of flowers <code>x</code> in the first lane must be in the range <code>[1,n]</code>.</li>
	<li>The number of flowers <code>y</code> in the second lane must be in the range <code>[1,m]</code>.</li>
</ul>

<p>Return <em>the number of possible pairs</em> <code>(x, y)</code> <em>that satisfy the conditions mentioned in the statement</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, m = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> The following pairs satisfy conditions described in the statement: (1,2), (3,2), (2,1).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, m = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> No pairs satisfy the conditions described in the statement.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
</ul>
