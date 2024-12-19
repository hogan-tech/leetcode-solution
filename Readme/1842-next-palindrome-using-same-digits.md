<h2><a href="https://leetcode.com/problems/next-palindrome-using-same-digits/">1842. Next Palindrome Using Same Digits</a></h2><h3>Hard</h3><hr><div><p>You are given a numeric string <code>num</code>, representing a very large <strong>palindrome</strong>.</p>

<p>Return<em> the <strong>smallest palindrome larger than </strong></em><code>num</code><em> that can be created by rearranging its digits. If no such palindrome exists, return an empty string </em><code>""</code>.</p>

<p>A <strong>palindrome</strong> is a number that reads the same backward as forward.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> num = "1221"
<strong>Output:</strong> "2112"
<strong>Explanation:</strong>&nbsp;The next palindrome larger than "1221" is "2112".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> num = "32123"
<strong>Output:</strong> ""
<strong>Explanation:</strong>&nbsp;No palindromes larger than "32123" can be made by rearranging the digits.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> num = "45544554"
<strong>Output:</strong> "54455445"
<strong>Explanation:</strong> The next palindrome larger than "45544554" is "54455445".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 10<sup>5</sup></code></li>
	<li><code>num</code> is a <strong>palindrome</strong>.</li>
</ul>
</div>