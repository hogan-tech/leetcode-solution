<h2> 1478 176
1366. Rank Teams by Votes</h2><hr><div><p>In a special ranking system, each voter gives a rank from highest to lowest to all teams participating in the competition.</p>

<p>The ordering of teams is decided by who received the most position-one votes. If two or more teams tie in the first position, we consider the second position to resolve the conflict, if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after considering all positions, we rank them alphabetically based on their team letter.</p>

<p>You are given an array of strings <code>votes</code> which is the votes of all voters in the ranking systems. Sort all teams according to the ranking system described above.</p>

<p>Return <em>a string of all teams <strong>sorted</strong> by the ranking system</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> votes = ["ABC","ACB","ABC","ACB","ACB"]
<strong>Output:</strong> "ACB"
<strong>Explanation:</strong> 
Team A was ranked first place by 5 voters. No other team was voted as first place, so team A is the first team.
Team B was ranked second by 2 voters and ranked third by 3 voters.
Team C was ranked second by 3 voters and ranked third by 2 voters.
As most of the voters ranked C second, team C is the second team, and team B is the third.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> votes = ["WXYZ","XYZW"]
<strong>Output:</strong> "XWYZ"
<strong>Explanation:</strong>
X is the winner due to the tie-breaking rule. X has the same votes as W for the first position, but X has one vote in the second position, while W does not have any votes in the second position. 
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
<strong>Output:</strong> "ZMNAGUEDSJYLBOPHRQICWFXTVK"
<strong>Explanation:</strong> Only one voter, so their votes are used for the ranking.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= votes.length &lt;= 1000</code></li>
	<li><code>1 &lt;= votes[i].length &lt;= 26</code></li>
	<li><code>votes[i].length == votes[j].length</code> for <code>0 &lt;= i, j &lt; votes.length</code>.</li>
	<li><code>votes[i][j]</code> is an English <strong>uppercase</strong> letter.</li>
	<li>All characters of <code>votes[i]</code> are unique.</li>
	<li>All the characters that occur in <code>votes[0]</code> <strong>also occur</strong> in <code>votes[j]</code> where <code>1 &lt;= j &lt; votes.length</code>.</li>
</ul>
</div>