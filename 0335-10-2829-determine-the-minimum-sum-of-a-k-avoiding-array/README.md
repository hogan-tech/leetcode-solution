<h2> 335 10
2829. Determine the Minimum Sum of a k-avoiding Array</h2><hr><div><p>You are given two integers,&nbsp;<code>n</code> and <code>k</code>.</p>

<p>An array of <strong>distinct</strong> positive integers is called a <b>k-avoiding</b> array if there does not exist any pair of distinct elements that sum to <code>k</code>.</p>

<p>Return <em>the <strong>minimum</strong> possible sum of a k-avoiding array of length </em><code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> n = 5, k = 4
<strong>Output:</strong> 18
<strong>Explanation:</strong> Consider the k-avoiding array [1,2,4,5,6], which has a sum of 18.
It can be proven that there is no k-avoiding array with a sum less than 18.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> n = 2, k = 6
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can construct the array [1,2], which has a sum of 3.
It can be proven that there is no k-avoiding array with a sum less than 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, k &lt;= 50</code></li>
</ul>
</div>