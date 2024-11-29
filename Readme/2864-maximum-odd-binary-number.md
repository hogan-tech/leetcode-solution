<h2><a href="https://leetcode.com/problems/maximum-odd-binary-number/">2864. Maximum Odd Binary Number</a></h2><h3>Easy</h3><hr><div><p>You are given a <strong>binary</strong> string <code>s</code> that contains at least one <code>'1'</code>.</p>

<p>You have to <strong>rearrange</strong> the bits in such a way that the resulting binary number is the <strong>maximum odd binary number</strong> that can be created from this combination.</p>

<p>Return <em>a string representing the maximum odd binary number that can be created from the given combination.</em></p>

<p><strong>Note </strong>that the resulting string <strong>can</strong> have leading zeros.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "010"
<strong>Output:</strong> "001"
<strong>Explanation:</strong> Because there is just one '1', it must be in the last position. So the answer is "001".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "0101"
<strong>Output:</strong> "1001"
<strong>Explanation: </strong>One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists only of <code>'0'</code> and <code>'1'</code>.</li>
	<li><code>s</code> contains at least one <code>'1'</code>.</li>
</ul>
</div>