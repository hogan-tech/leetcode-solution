<h2> 628 49
3223. Minimum Length of String After Operations</h2><hr><div><p>You are given a string <code>s</code>.</p>

<p>You can perform the following process on <code>s</code> <strong>any</strong> number of times:</p>

<ul>
	<li>Choose an index <code>i</code> in the string such that there is <strong>at least</strong> one character to the left of index <code>i</code> that is equal to <code>s[i]</code>, and <strong>at least</strong> one character to the right that is also equal to <code>s[i]</code>.</li>
	<li>Delete the <strong>closest</strong> character to the <strong>left</strong> of index <code>i</code> that is equal to <code>s[i]</code>.</li>
	<li>Delete the <strong>closest</strong> character to the <strong>right</strong> of index <code>i</code> that is equal to <code>s[i]</code>.</li>
</ul>

<p>Return the <strong>minimum</strong> length of the final string <code>s</code> that you can achieve.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "abaacbcbb"</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong><br>
We do the following operations:</p>

<ul>
	<li>Choose index 2, then remove the characters at indices 0 and 3. The resulting string is <code>s = "bacbcbb"</code>.</li>
	<li>Choose index 3, then remove the characters at indices 0 and 5. The resulting string is <code>s = "acbcb"</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "aa"</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong><br>
We cannot perform any operations, so we return the length of the original string.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>
</div>