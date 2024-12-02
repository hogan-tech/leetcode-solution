<h2><a href="https://leetcode.com/problems/find-the-celebrity/">277. Find the Celebrity</a></h2><h3>Medium</h3><hr><div><p>Suppose you are at a party with <code>n</code> people labeled from <code>0</code> to <code>n - 1</code> and among them, there may exist one celebrity. The definition of a celebrity is that all the other <code>n - 1</code> people know the celebrity, but the celebrity does not know any of them.</p>

<p>Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).</p>

<p>You are given an integer <code>n</code> and a helper function <code>bool knows(a, b)</code> that tells you whether <code>a</code> knows <code>b</code>. Implement a function <code>int findCelebrity(n)</code>. There will be exactly one celebrity if they are at the party.</p>

<p>Return <em>the celebrity's label if there is a celebrity at the party</em>. If there is no celebrity, return <code>-1</code>.</p>

<p><strong>Note</strong> that the <code>n x n</code> 2D array <code>graph</code> given as input is <strong>not</strong> directly available to you, and instead <strong>only</strong> accessible through the helper function <code>knows</code>. <code>graph[i][j] == 1</code> represents person <code>i</code> knows person <code>j</code>, wherease <code>graph[i][j] == 0</code> represents person <code>j</code> does not know person <code>i</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/01/19/g1.jpg" style="width: 224px; height: 145px;">
<pre><strong>Input:</strong> graph = [[1,1,0],[0,1,0],[1,1,1]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/01/19/g2.jpg" style="width: 224px; height: 145px;">
<pre><strong>Input:</strong> graph = [[1,0,1],[1,1,0],[0,1,1]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no celebrity.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == graph.length == graph[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>graph[i][j]</code> is <code>0</code> or <code>1</code>.</li>
	<li><code>graph[i][i] == 1</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If the maximum number of allowed calls to the API <code>knows</code> is <code>3 * n</code>, could you find a solution without exceeding the maximum number of calls?</p>
</div>