<h2><a href="https://leetcode.com/problems/minimum-window-subsequence/">727. Minimum Window Subsequence</a></h2><h3>Hard</h3><hr><div><p>Given strings <code>s1</code> and <code>s2</code>, return <em>the minimum contiguous&nbsp;substring part of </em><code>s1</code><em>, so that </em><code>s2</code><em> is a subsequence of the part</em>.</p>

<p>If there is no such window in <code>s1</code> that covers all characters in <code>s2</code>, return the empty string <code>""</code>. If there are multiple such minimum-length windows, return the one with the <strong>left-most starting index</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s1 = "abcdebdde", s2 = "bde"
<strong>Output:</strong> "bcde"
<strong>Explanation:</strong> 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of s2 in the window must occur in order.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
<strong>Output:</strong> ""
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s1.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= s2.length &lt;= 100</code></li>
	<li><code>s1</code> and <code>s2</code> consist of lowercase English letters.</li>
</ul>
</div>