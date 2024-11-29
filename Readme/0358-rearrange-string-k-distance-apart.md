<h2><a href="https://leetcode.com/problems/rearrange-string-k-distance-apart/">358. Rearrange String k Distance Apart</a></h2><h3>Hard</h3><hr><div><p>Given a string <code>s</code> and an integer <code>k</code>, rearrange <code>s</code> such that the same characters are <strong>at least</strong> distance <code>k</code> from each other. If it is not possible to rearrange the string, return an empty string <code>""</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "aabbcc", k = 3
<strong>Output:</strong> "abcabc"
<strong>Explanation:</strong> The same letters are at least a distance of 3 from each other.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "aaabc", k = 3
<strong>Output:</strong> ""
<strong>Explanation:</strong> It is not possible to rearrange the string.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "aaadbbcc", k = 2
<strong>Output:</strong> "abacabcd"
<strong>Explanation:</strong> The same letters are at least a distance of 2 from each other.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
</ul>
</div>