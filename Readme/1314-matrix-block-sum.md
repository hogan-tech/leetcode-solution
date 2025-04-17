<h2><a href="https://leetcode.com/problems/matrix-block-sum">1242. Matrix Block Sum</a></h2><h3>Medium</h3><hr><p>Given a <code>m x n</code> matrix <code>mat</code> and an integer <code>k</code>, return <em>a matrix</em> <code>answer</code> <em>where each</em> <code>answer[i][j]</code> <em>is the sum of all elements</em> <code>mat[r][c]</code> <em>for</em>:</p>

<ul>
	<li><code>i - k &lt;= r &lt;= i + k,</code></li>
	<li><code>j - k &lt;= c &lt;= j + k</code>, and</li>
	<li><code>(r, c)</code> is a valid position in the matrix.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
<strong>Output:</strong> [[12,21,16],[27,45,33],[24,39,28]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
<strong>Output:</strong> [[45,45,45],[45,45,45],[45,45,45]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m ==&nbsp;mat.length</code></li>
	<li><code>n ==&nbsp;mat[i].length</code></li>
	<li><code>1 &lt;= m, n, k &lt;= 100</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 100</code></li>
</ul>
