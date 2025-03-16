<h2> 1032 470
1003. Check If Word Is Valid After Substitutions</h2><hr><div><p>Given a string <code>s</code>, determine if it is <strong>valid</strong>.</p>

<p>A string <code>s</code> is <strong>valid</strong> if, starting with an empty string <code>t = ""</code>, you can <strong>transform </strong><code>t</code><strong> into </strong><code>s</code> after performing the following operation <strong>any number of times</strong>:</p>

<ul>
	<li>Insert string <code>"abc"</code> into any position in <code>t</code>. More formally, <code>t</code> becomes <code>t<sub>left</sub> + "abc" + t<sub>right</sub></code>, where <code>t == t<sub>left</sub> + t<sub>right</sub></code>. Note that <code>t<sub>left</sub></code> and <code>t<sub>right</sub></code> may be <strong>empty</strong>.</li>
</ul>

<p>Return <code>true</code> <em>if </em><code>s</code><em> is a <strong>valid</strong> string, otherwise, return</em> <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "aabcbc"
<strong>Output:</strong> true
<strong>Explanation:</strong>
"" -&gt; "<u>abc</u>" -&gt; "a<u>abc</u>bc"
Thus, "aabcbc" is valid.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "abcabcababcc"
<strong>Output:</strong> true
<strong>Explanation:</strong>
"" -&gt; "<u>abc</u>" -&gt; "abc<u>abc</u>" -&gt; "abcabc<u>abc</u>" -&gt; "abcabcab<u>abc</u>c"
Thus, "abcabcababcc" is valid.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "abccba"
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to get "abccba" using the operation.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of letters <code>'a'</code>, <code>'b'</code>, and <code>'c'</code></li>
</ul>
</div>