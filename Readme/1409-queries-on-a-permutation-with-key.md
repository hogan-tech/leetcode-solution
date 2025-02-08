<h2> 503 636
1409. Queries on a Permutation With Key</h2><hr><div><p>Given the array <code>queries</code> of positive integers between <code>1</code> and <code>m</code>, you have to process all <code>queries[i]</code> (from <code>i=0</code> to <code>i=queries.length-1</code>) according to the following rules:</p>

<ul>
	<li>In the beginning, you have the permutation <code>P=[1,2,3,...,m]</code>.</li>
	<li>For the current <code>i</code>, find the position of <code>queries[i]</code> in the permutation <code>P</code> (<strong>indexing from 0</strong>) and then move this at the beginning of the permutation <code>P</code>. Notice that the position of <code>queries[i]</code> in <code>P</code> is the result for <code>queries[i]</code>.</li>
</ul>

<p>Return an array containing the result for the given <code>queries</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> queries = [3,1,2,1], m = 5
<strong>Output:</strong> [2,1,2,1] 
<strong>Explanation:</strong> The queries are processed as follow: 
For i=0: queries[i]=3, P=[1,2,3,4,5], position of 3 in P is <strong>2</strong>, then we move 3 to the beginning of P resulting in P=[3,1,2,4,5]. 
For i=1: queries[i]=1, P=[3,1,2,4,5], position of 1 in P is <strong>1</strong>, then we move 1 to the beginning of P resulting in P=[1,3,2,4,5]. 
For i=2: queries[i]=2, P=[1,3,2,4,5], position of 2 in P is <strong>2</strong>, then we move 2 to the beginning of P resulting in P=[2,1,3,4,5]. 
For i=3: queries[i]=1, P=[2,1,3,4,5], position of 1 in P is <strong>1</strong>, then we move 1 to the beginning of P resulting in P=[1,2,3,4,5]. 
Therefore, the array containing the result is [2,1,2,1].  
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> queries = [4,1,2,2], m = 4
<strong>Output:</strong> [3,1,2,0]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> queries = [7,5,5,8,3], m = 8
<strong>Output:</strong> [6,5,0,7,5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m &lt;= 10^3</code></li>
	<li><code>1 &lt;= queries.length &lt;= m</code></li>
	<li><code>1 &lt;= queries[i] &lt;= m</code></li>
</ul>
</div>