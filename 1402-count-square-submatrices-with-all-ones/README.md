<h2><a href="https://leetcode.com/problems/count-square-submatrices-with-all-ones">1402. Count Square Submatrices with All Ones</a></h2><h3>Medium</h3><hr><p>Given a <code>m * n</code> matrix of ones and zeros, return how many <strong>square</strong> submatrices have all ones.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> matrix =
[
&nbsp; [0,1,1,1],
&nbsp; [1,1,1,1],
&nbsp; [0,1,1,1]
]
<strong>Output:</strong> 15
<strong>Explanation:</strong> 
There are <strong>10</strong> squares of side 1.
There are <strong>4</strong> squares of side 2.
There is  <strong>1</strong> square of side 3.
Total number of squares = 10 + 4 + 1 = <strong>15</strong>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
<strong>Output:</strong> 7
<strong>Explanation:</strong> 
There are <b>6</b> squares of side 1.  
There is <strong>1</strong> square of side 2. 
Total number of squares = 6 + 1 = <b>7</b>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length&nbsp;&lt;= 300</code></li>
	<li><code>1 &lt;= arr[0].length&nbsp;&lt;= 300</code></li>
	<li><code>0 &lt;= arr[i][j] &lt;= 1</code></li>
</ul>
