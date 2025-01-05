<h2> 4929 1649
953. Verifying an Alien Dictionary</h2><hr><div><p>In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different <code>order</code>. The <code>order</code> of the alphabet is some permutation of lowercase letters.</p>

<p>Given a sequence of <code>words</code> written in the alien language, and the <code>order</code> of the alphabet, return <code>true</code> if and only if the given <code>words</code> are sorted lexicographically in this alien language.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
<strong>Output:</strong> true
<strong>Explanation: </strong>As 'h' comes before 'l' in this language, then the sequence is sorted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
<strong>Output:</strong> false
<strong>Explanation: </strong>As 'd' comes after 'l' in this language, then words[0] &gt; words[1], hence the sequence is unsorted.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
<strong>Output:</strong> false
<strong>Explanation: </strong>The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" &gt; "app", because 'l' &gt; '∅', where '∅' is defined as the blank character which is less than any other character (<a href="https://en.wikipedia.org/wiki/Lexicographical_order" target="_blank">More info</a>).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 20</code></li>
	<li><code>order.length == 26</code></li>
	<li>All characters in <code>words[i]</code> and <code>order</code> are English lowercase letters.</li>
</ul>
</div>