<h2> 381 108
1065. Index Pairs of a String</h2><hr><div><p>Given a string <code>text</code> and an array of strings <code>words</code>, return <em>an array of all index pairs </em><code>[i, j]</code><em> so that the substring </em><code>text[i...j]</code><em> is in <code>words</code></em>.</p>

<p>Return the pairs <code>[i, j]</code> in sorted order (i.e., sort them by their first coordinate, and in case of ties sort them by their second coordinate).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
<strong>Output:</strong> [[3,7],[9,13],[10,17]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> text = "ababa", words = ["aba","ab"]
<strong>Output:</strong> [[0,1],[0,2],[2,3],[2,4]]
<strong>Explanation:</strong> Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 100</code></li>
	<li><code>1 &lt;= words.length &lt;= 20</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 50</code></li>
	<li><code>text</code> and <code>words[i]</code> consist of lowercase English letters.</li>
	<li>All the strings of <code>words</code> are <strong>unique</strong>.</li>
</ul>
</div>