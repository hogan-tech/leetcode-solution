<h2> 1031 68
1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K</h2><hr><div><p>Given an integer&nbsp;<code>k</code>, <em>return the minimum number of Fibonacci numbers whose sum is equal to </em><code>k</code>. The same Fibonacci number can be used multiple times.</p>

<p>The Fibonacci numbers are defined as:</p>

<ul>
	<li><code>F<sub>1</sub> = 1</code></li>
	<li><code>F<sub>2</sub> = 1</code></li>
	<li><code>F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub></code> for <code>n &gt; 2.</code></li>
</ul>
It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to <code>k</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> k = 7
<strong>Output:</strong> 2 
<strong>Explanation:</strong> The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
For k = 7 we can use 2 + 5 = 7.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> k = 10
<strong>Output:</strong> 2 
<strong>Explanation:</strong> For k = 10 we can use 2 + 8 = 10.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> k = 19
<strong>Output:</strong> 3 
<strong>Explanation:</strong> For k = 19 we can use 1 + 5 + 13 = 19.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>
</div>