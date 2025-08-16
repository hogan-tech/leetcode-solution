<h2><a href="https://leetcode.com/problems/maximum-69-number">1448. Maximum 69 Number</a></h2><h3>Easy</h3><hr><p>You are given a positive integer <code>num</code> consisting only of digits <code>6</code> and <code>9</code>.</p>

<p>Return <em>the maximum number you can get by changing <strong>at most</strong> one digit (</em><code>6</code><em> becomes </em><code>9</code><em>, and </em><code>9</code><em> becomes </em><code>6</code><em>)</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 9669
<strong>Output:</strong> 9969
<strong>Explanation:</strong> 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 9996
<strong>Output:</strong> 9999
<strong>Explanation:</strong> Changing the last digit 6 to 9 results in the maximum number.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = 9999
<strong>Output:</strong> 9999
<strong>Explanation:</strong> It is better not to apply any change.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>4</sup></code></li>
	<li><code>num</code>&nbsp;consists of only <code>6</code> and <code>9</code> digits.</li>
</ul>
