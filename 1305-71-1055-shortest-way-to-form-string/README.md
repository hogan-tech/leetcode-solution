<h2> 1305 71
1055. Shortest Way to Form String</h2><hr><div><p>A <strong>subsequence</strong> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code>"ace"</code> is a subsequence of <code>"<u>a</u>b<u>c</u>d<u>e</u>"</code> while <code>"aec"</code> is not).</p>

<p>Given two strings <code>source</code> and <code>target</code>, return <em>the minimum number of <strong>subsequences</strong> of </em><code>source</code><em> such that their concatenation equals </em><code>target</code>. If the task is impossible, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> source = "abc", target = "abcbc"
<strong>Output:</strong> 2
<strong>Explanation:</strong> The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> source = "abc", target = "acdbc"
<strong>Output:</strong> -1
<strong>Explanation:</strong> The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> source = "xyz", target = "xzyxz"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The target string can be constructed as follows "xz" + "y" + "xz".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= source.length, target.length &lt;= 1000</code></li>
	<li><code>source</code> and <code>target</code> consist of lowercase English letters.</li>
</ul>
</div>