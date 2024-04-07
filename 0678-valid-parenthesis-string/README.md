<h2><a href="https://leetcode.com/problems/valid-parenthesis-string/">678. Valid Parenthesis String</a></h2><h3>Medium</h3><hr><div><p>Given a string <code>s</code> containing only three types of characters: <code>'('</code>, <code>')'</code> and <code>'*'</code>, return <code>true</code> <em>if</em> <code>s</code> <em>is <strong>valid</strong></em>.</p>

<p>The following rules define a <strong>valid</strong> string:</p>

<ul>
	<li>Any left parenthesis <code>'('</code> must have a corresponding right parenthesis <code>')'</code>.</li>
	<li>Any right parenthesis <code>')'</code> must have a corresponding left parenthesis <code>'('</code>.</li>
	<li>Left parenthesis <code>'('</code> must go before the corresponding right parenthesis <code>')'</code>.</li>
	<li><code>'*'</code> could be treated as a single right parenthesis <code>')'</code> or a single left parenthesis <code>'('</code> or an empty string <code>""</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "()"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "(*)"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> s = "(*))"
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s[i]</code> is <code>'('</code>, <code>')'</code> or <code>'*'</code>.</li>
</ul>
</div>