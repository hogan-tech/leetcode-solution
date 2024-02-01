<h2><a href="https://leetcode.com/problems/flip-game/">293. Flip Game</a></h2><h3>Easy</h3><hr><div><p>You are playing a Flip Game with your friend.</p>

<p>You are given a string <code>currentState</code> that contains only <code>'+'</code> and <code>'-'</code>. You and your friend take turns to flip <strong>two consecutive</strong> <code>"++"</code> into <code>"--"</code>. The game ends when a person can no longer make a move, and therefore the other person will be the winner.</p>

<p>Return all possible states of the string <code>currentState</code> after <strong>one valid move</strong>. You may return the answer in <strong>any order</strong>. If there is no valid move, return an empty list <code>[]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> currentState = "++++"
<strong>Output:</strong> ["--++","+--+","++--"]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> currentState = "+"
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= currentState.length &lt;= 500</code></li>
	<li><code>currentState[i]</code> is either <code>'+'</code> or <code>'-'</code>.</li>
</ul>
</div>