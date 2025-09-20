<h2><a href="https://leetcode.com/problems/word-pattern-ii">291. Word Pattern II</a></h2><h3>Medium</h3><hr><p>Given a <code>pattern</code> and a string <code>s</code>, return <code>true</code><em> if </em><code>s</code><em> <strong>matches</strong> the </em><code>pattern</code><em>.</em></p>

<p>A string <code>s</code> <b>matches</b> a <code>pattern</code> if there is some <strong>bijective mapping</strong> of single characters to <strong>non-empty</strong> strings such that if each character in <code>pattern</code> is replaced by the string it maps to, then the resulting string is <code>s</code>. A <strong>bijective mapping</strong> means that no two characters map to the same string, and no character maps to two different strings.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> pattern = &quot;abab&quot;, s = &quot;redblueredblue&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> One possible mapping is as follows:
&#39;a&#39; -&gt; &quot;red&quot;
&#39;b&#39; -&gt; &quot;blue&quot;</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> pattern = &quot;aaaa&quot;, s = &quot;asdasdasdasd&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> One possible mapping is as follows:
&#39;a&#39; -&gt; &quot;asd&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> pattern = &quot;aabb&quot;, s = &quot;xyzabcxzyabc&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= pattern.length, s.length &lt;= 20</code></li>
	<li><code>pattern</code> and <code>s</code> consist of only lowercase English letters.</li>
</ul>
