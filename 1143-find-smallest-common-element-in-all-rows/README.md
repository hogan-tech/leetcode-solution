<h2><a href="https://leetcode.com/problems/find-smallest-common-element-in-all-rows">1143. Find Smallest Common Element in All Rows</a></h2><h3>Medium</h3><hr><p>Given an <code>m x n</code> matrix <code>mat</code> where every row is sorted in <strong>strictly</strong> <strong>increasing</strong> order, return <em>the <strong>smallest common element</strong> in all rows</em>.</p>

<p>If there is no common element, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
<strong>Output:</strong> 5
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> mat = [[1,2,3],[2,3,4],[2,3,5]]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 10<sup>4</sup></code></li>
	<li><code>mat[i]</code> is sorted in strictly increasing order.</li>
</ul>
