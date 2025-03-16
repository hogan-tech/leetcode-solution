<h2> 143 7
3039. Apply Operations to Make String Empty</h2><hr><div><p>You are given a string <code>s</code>.</p>

<p>Consider performing the following operation until <code>s</code> becomes <strong>empty</strong>:</p>

<ul>
	<li>For <strong>every</strong> alphabet character from <code>'a'</code> to <code>'z'</code>, remove the <strong>first</strong> occurrence of that character in <code>s</code> (if it exists).</li>
</ul>

<p>For example, let initially <code>s = "aabcbbca"</code>. We do the following operations:</p>

<ul>
	<li>Remove the underlined characters <code>s = "<u><strong>a</strong></u>a<strong><u>bc</u></strong>bbca"</code>. The resulting string is <code>s = "abbca"</code>.</li>
	<li>Remove the underlined characters <code>s = "<u><strong>ab</strong></u>b<u><strong>c</strong></u>a"</code>. The resulting string is <code>s = "ba"</code>.</li>
	<li>Remove the underlined characters <code>s = "<u><strong>ba</strong></u>"</code>. The resulting string is <code>s = ""</code>.</li>
</ul>

<p>Return <em>the value of the string </em><code>s</code><em> right <strong>before</strong> applying the <strong>last</strong> operation</em>. In the example above, answer is <code>"ba"</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "aabcbbca"
<strong>Output:</strong> "ba"
<strong>Explanation:</strong> Explained in the statement.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "abcd"
<strong>Output:</strong> "abcd"
<strong>Explanation:</strong> We do the following operation:
- Remove the underlined characters s = "<u><strong>abcd</strong></u>". The resulting string is s = "".
The string just before the last operation is "abcd".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>
</div>