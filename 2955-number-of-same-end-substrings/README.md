<h2><a href="https://leetcode.com/problems/number-of-same-end-substrings/">2955. Number of Same-End Substrings</a></h2><h3>Medium</h3><hr><div><p>You are given a <strong>0-indexed</strong> string <code>s</code>, and a 2D array of integers <code>queries</code>, where <code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code> indicates a substring of <code>s</code> starting from the index <code>l<sub>i</sub></code> and ending at the index <code>r<sub>i</sub></code> (both <strong>inclusive</strong>), i.e. <code>s[l<sub>i</sub>..r<sub>i</sub>]</code>.</p>

<p>Return <em>an array </em><code>ans</code><em> where</em> <code>ans[i]</code> <em>is the number of <strong>same-end</strong> substrings of</em> <code>queries[i]</code>.</p>

<p>A <strong>0-indexed</strong> string <code>t</code> of length <code>n</code> is called <strong>same-end</strong> if it has the same character at both of its ends, i.e., <code>t[0] == t[n - 1]</code>.</p>

<p>A <b>substring</b> is a contiguous non-empty sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "abcaab", queries = [[0,0],[1,4],[2,5],[0,5]]
<strong>Output:</strong> [1,5,5,10]
<strong>Explanation:</strong> Here is the same-end substrings of each query:
1<sup>st</sup> query: s[0..0] is "a" which has 1 same-end substring: "<strong><u>a</u></strong>".
2<sup>nd</sup> query: s[1..4] is "bcaa" which has 5 same-end substrings: "<strong><u>b</u></strong>caa", "b<strong><u>c</u></strong>aa", "bc<strong><u>a</u></strong>a", "bca<strong><u>a</u></strong>", "bc<strong><u>aa</u></strong>".
3<sup>rd</sup> query: s[2..5] is "caab" which has 5 same-end substrings: "<strong><u>c</u></strong>aab", "c<strong><u>a</u></strong>ab", "ca<strong><u>a</u></strong>b", "caa<strong><u>b</u></strong>", "c<strong><u>aa</u></strong>b".
4<sup>th</sup> query: s[0..5] is "abcaab" which has 10 same-end substrings: "<strong><u>a</u></strong>bcaab", "a<strong><u>b</u></strong>caab", "ab<strong><u>c</u></strong>aab", "abc<strong><u>a</u></strong>ab", "abca<strong><u>a</u></strong>b", "abcaa<strong><u>b</u></strong>", "abc<strong><u>aa</u></strong>b", "<strong><u>abca</u></strong>ab", "<strong><u>abcaa</u></strong>b", "a<strong><u>bcaab</u></strong>".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "abcd", queries = [[0,3]]
<strong>Output:</strong> [4]
<strong>Explanation:</strong> The only query is s[0..3] which is "abcd". It has 4 same-end substrings: "<strong><u>a</u></strong>bcd", "a<strong><u>b</u></strong>cd", "ab<strong><u>c</u></strong>d", "abc<strong><u>d</u></strong>".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
	<li><code>1 &lt;= queries.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code></li>
	<li><code>0 &lt;= l<sub>i</sub> &lt;= r<sub>i</sub> &lt; s.length</code></li>
</ul>
</div>