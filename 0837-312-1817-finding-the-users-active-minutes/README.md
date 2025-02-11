<h2> 837 312
1817. Finding the Users Active Minutes</h2><hr><div><p>You are given the logs for users' actions on LeetCode, and an integer <code>k</code>. The logs are represented by a 2D integer array <code>logs</code> where each <code>logs[i] = [ID<sub>i</sub>, time<sub>i</sub>]</code> indicates that the user with <code>ID<sub>i</sub></code> performed an action at the minute <code>time<sub>i</sub></code>.</p>

<p><strong>Multiple users</strong> can perform actions simultaneously, and a single user can perform <strong>multiple actions</strong> in the same minute.</p>

<p>The <strong>user active minutes (UAM)</strong> for a given user is defined as the <strong>number of unique minutes</strong> in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.</p>

<p>You are to calculate a <strong>1-indexed</strong> array <code>answer</code> of size <code>k</code> such that, for each <code>j</code> (<code>1 &lt;= j &lt;= k</code>), <code>answer[j]</code> is the <strong>number of users</strong> whose <strong>UAM</strong> equals <code>j</code>.</p>

<p>Return <i>the array </i><code>answer</code><i> as described above</i>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
<strong>Output:</strong> [0,2,0,0,0]
<strong>Explanation:</strong>
The user with ID=0 performed actions at minutes 5, 2, and 5 again. Hence, they have a UAM of 2 (minute 5 is only counted once).
The user with ID=1 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
Since both users have a UAM of 2, answer[2] is 2, and the remaining answer[j] values are 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> logs = [[1,1],[2,2],[2,3]], k = 4
<strong>Output:</strong> [1,1,0,0]
<strong>Explanation:</strong>
The user with ID=1 performed a single action at minute 1. Hence, they have a UAM of 1.
The user with ID=2 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
There is one user with a UAM of 1 and one with a UAM of 2.
Hence, answer[1] = 1, answer[2] = 1, and the remaining values are 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= logs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= ID<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= time<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>k</code> is in the range <code>[The maximum <strong>UAM</strong> for a user, 10<sup>5</sup>]</code>.</li>
</ul>
</div>