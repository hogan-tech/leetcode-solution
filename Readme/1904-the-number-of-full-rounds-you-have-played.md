<h2><a href="https://leetcode.com/problems/the-number-of-full-rounds-you-have-played">2033. The Number of Full Rounds You Have Played</a></h2><h3>Medium</h3><hr><p>You are participating in an online chess tournament. There is a chess round that starts every <code>15</code> minutes. The first round of the day starts at <code>00:00</code>, and after every <code>15</code> minutes, a new round starts.</p>

<ul>
	<li>For example, the second round starts at <code>00:15</code>, the fourth round starts at <code>00:45</code>, and the seventh round starts at <code>01:30</code>.</li>
</ul>

<p>You are given two strings <code>loginTime</code> and <code>logoutTime</code> where:</p>

<ul>
	<li><code>loginTime</code> is the time you will login to the game, and</li>
	<li><code>logoutTime</code> is the time you will logout from the game.</li>
</ul>

<p>If <code>logoutTime</code> is <strong>earlier</strong> than <code>loginTime</code>, this means you have played from <code>loginTime</code> to midnight and from midnight to <code>logoutTime</code>.</p>

<p>Return <em>the number of full chess rounds you have played in the tournament</em>.</p>

<p><strong>Note:</strong>&nbsp;All the given times follow the 24-hour clock. That means the first round of the day starts at <code>00:00</code> and the last round of the day starts at <code>23:45</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> loginTime = &quot;09:31&quot;, logoutTime = &quot;10:14&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> You played one full round from 09:45 to 10:00.
You did not play the full round from 09:30 to 09:45 because you logged in at 09:31 after it began.
You did not play the full round from 10:00 to 10:15 because you logged out at 10:14 before it ended.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> loginTime = &quot;21:30&quot;, logoutTime = &quot;03:00&quot;
<strong>Output:</strong> 22
<strong>Explanation:</strong> You played 10 full rounds from 21:30 to 00:00 and 12 full rounds from 00:00 to 03:00.
10 + 12 = 22.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>loginTime</code> and <code>logoutTime</code> are in the format <code>hh:mm</code>.</li>
	<li><code>00 &lt;= hh &lt;= 23</code></li>
	<li><code>00 &lt;= mm &lt;= 59</code></li>
	<li><code>loginTime</code> and <code>logoutTime</code> are not equal.</li>
</ul>
