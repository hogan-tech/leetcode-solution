<h2><a href="https://leetcode.com/problems/alien-dictionary">269. Alien Dictionary</a></h2><h3>Hard</h3><hr><p>There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.</p>

<p>You are given a list of strings <code>words</code> from the alien language&#39;s dictionary. Now it is claimed that the strings in <code>words</code> are <span data-keyword="lexicographically-smaller-string-alien"><strong>sorted lexicographically</strong></span> by the rules of this new language.</p>

<p>If this claim is incorrect, and the given arrangement of string in&nbsp;<code>words</code>&nbsp;cannot correspond to any order of letters,&nbsp;return&nbsp;<code>&quot;&quot;.</code></p>

<p>Otherwise, return <em>a string of the unique letters in the new alien language sorted in <strong>lexicographically increasing order</strong> by the new language&#39;s rules</em><em>. </em>If there are multiple solutions, return<em> <strong>any of them</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;wrt&quot;,&quot;wrf&quot;,&quot;er&quot;,&quot;ett&quot;,&quot;rftt&quot;]
<strong>Output:</strong> &quot;wertf&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;z&quot;,&quot;x&quot;]
<strong>Output:</strong> &quot;zx&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;z&quot;,&quot;x&quot;,&quot;z&quot;]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> The order is invalid, so return <code>&quot;&quot;</code>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> consists of only lowercase English letters.</li>
</ul>
