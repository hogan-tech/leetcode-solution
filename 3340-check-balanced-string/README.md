<h2><a href="https://leetcode.com/problems/check-balanced-string/">3340. Check Balanced String</a></h2><h3>Easy</h3><hr><div><p>You are given a string <code>num</code> consisting of only digits. A string of digits is called <b>balanced </b>if the sum of the digits at even indices is equal to the sum of digits at odd indices.</p>

<p>Return <code>true</code> if <code>num</code> is <strong>balanced</strong>, otherwise return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> num<span class="example-io"> = "1234"</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The sum of digits at even indices is <code>1 + 3 == 4</code>, and the sum of digits at odd indices is <code>2 + 4 == 6</code>.</li>
	<li>Since 4 is not equal to 6, <code>num</code> is not balanced.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> num<span class="example-io"> = "24123"</span></p>

<p><strong>Output:</strong> true</p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The sum of digits at even indices is <code>2 + 1 + 3 == 6</code>, and the sum of digits at odd indices is <code>4 + 2 == 6</code>.</li>
	<li>Since both are equal the <code>num</code> is balanced.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= num.length &lt;= 100</code></li>
	<li><code><font face="monospace">num</font></code> consists of digits only</li>
</ul>
</div>