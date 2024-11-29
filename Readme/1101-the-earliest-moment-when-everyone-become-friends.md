<h2><a href="https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/">1101. The Earliest Moment When Everyone Become Friends</a></h2><h3>Medium</h3><hr><div><p>There are n people in a social group labeled from <code>0</code> to <code>n - 1</code>. You are given an array <code>logs</code> where <code>logs[i] = [timestamp<sub>i</sub>, x<sub>i</sub>, y<sub>i</sub>]</code> indicates that <code>x<sub>i</sub></code> and <code>y<sub>i</sub></code> will be friends at the time <code>timestamp<sub>i</sub></code>.</p>

<p>Friendship is <strong>symmetric</strong>. That means if <code>a</code> is friends with <code>b</code>, then <code>b</code> is friends with <code>a</code>. Also, person <code>a</code> is acquainted with a person <code>b</code> if <code>a</code> is friends with <code>b</code>, or <code>a</code> is a friend of someone acquainted with <code>b</code>.</p>

<p>Return <em>the earliest time for which every person became acquainted with every other person</em>. If there is no such earliest time, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
<strong>Output:</strong> 20190301
<strong>Explanation:</strong> 
The first event occurs at timestamp = 20190101, and after 0 and 1 become friends, we have the following friendship groups [0,1], [2], [3], [4], [5].
The second event occurs at timestamp = 20190104, and after 3 and 4 become friends, we have the following friendship groups [0,1], [2], [3,4], [5].
The third event occurs at timestamp = 20190107, and after 2 and 3 become friends, we have the following friendship groups [0,1], [2,3,4], [5].
The fourth event occurs at timestamp = 20190211, and after 1 and 5 become friends, we have the following friendship groups [0,1,5], [2,3,4].
The fifth event occurs at timestamp = 20190224, and as 2 and 4 are already friends, nothing happens.
The sixth event occurs at timestamp = 20190301, and after 0 and 3 become friends, we all become friends.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> At timestamp = 3, all the persons (i.e., 0, 1, 2, and 3) become friends.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= logs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>logs[i].length == 3</code></li>
	<li><code>0 &lt;= timestamp<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>x<sub>i</sub> != y<sub>i</sub></code></li>
	<li>All the values <code>timestamp<sub>i</sub></code> are <strong>unique</strong>.</li>
	<li>All the pairs <code>(x<sub>i</sub>, y<sub>i</sub>)</code> occur at most one time in the input.</li>
</ul>
</div>