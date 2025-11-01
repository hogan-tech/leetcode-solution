<h2><a href="https://leetcode.com/problems/maximum-number-of-ones">1152. Maximum Number of Ones</a></h2><h3>Hard</h3><hr><p>Consider a matrix <code>M</code> with dimensions <code>width * height</code>, such that every cell has value <code>0</code>&nbsp;or <code>1</code>, and any <strong>square</strong>&nbsp;sub-matrix of <code>M</code> of size <code>sideLength * sideLength</code>&nbsp;has at most <code>maxOnes</code>&nbsp;ones.</p>

<p>Return the maximum possible number of ones that the matrix <code>M</code> can have.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> width = 3, height = 3, sideLength = 2, maxOnes = 1
<strong>Output:</strong> 4
<strong>Explanation:</strong>
In a 3*3 matrix, no 2*2 sub-matrix can have more than 1 one.
The best solution that has 4 ones is:
[1,0,1]
[0,0,0]
[1,0,1]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> width = 3, height = 3, sideLength = 2, maxOnes = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong>
[1,0,1]
[1,0,1]
[1,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= width, height &lt;= 100</code></li>
	<li><code>1 &lt;= sideLength &lt;= width, height</code></li>
	<li><code>0 &lt;= maxOnes &lt;= sideLength * sideLength</code></li>
</ul>
