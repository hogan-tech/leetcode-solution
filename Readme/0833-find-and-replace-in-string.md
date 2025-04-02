<h2> 1210 1040
833. Find And Replace in String</h2><hr><div><p>You are given a <strong>0-indexed</strong> string <code>s</code> that you must perform <code>k</code> replacement operations on. The replacement operations are given as three <strong>0-indexed</strong> parallel arrays, <code>indices</code>, <code>sources</code>, and <code>targets</code>, all of length <code>k</code>.</p>

<p>To complete the <code>i<sup>th</sup></code> replacement operation:</p>

<ol>
	<li>Check if the <strong>substring</strong> <code>sources[i]</code> occurs at index <code>indices[i]</code> in the <strong>original string</strong> <code>s</code>.</li>
	<li>If it does not occur, <strong>do nothing</strong>.</li>
	<li>Otherwise if it does occur, <strong>replace</strong> that substring with <code>targets[i]</code>.</li>
</ol>

<p>For example, if <code>s = "<u>ab</u>cd"</code>, <code>indices[i] = 0</code>, <code>sources[i] = "ab"</code>, and <code>targets[i] = "eee"</code>, then the result of this replacement will be <code>"<u>eee</u>cd"</code>.</p>

<p>All replacement operations must occur <strong>simultaneously</strong>, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will <strong>not overlap</strong>.</p>

<ul>
	<li>For example, a testcase with <code>s = "abc"</code>, <code>indices = [0, 1]</code>, and <code>sources = ["ab","bc"]</code> will not be generated because the <code>"ab"</code> and <code>"bc"</code> replacements overlap.</li>
</ul>

<p>Return <em>the <strong>resulting string</strong> after performing all replacement operations on </em><code>s</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters in a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/12/833-ex1.png" style="width: 411px; height: 251px;">
<pre><strong>Input:</strong> s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
<strong>Output:</strong> "eeebffff"
<strong>Explanation:</strong>
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/12/833-ex2-1.png" style="width: 411px; height: 251px;">
<pre><strong>Input:</strong> s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
<strong>Output:</strong> "eeecd"
<strong>Explanation:</strong>
"ab" occurs at index 0 in s, so we replace it with "eee".
"ec" does not occur at index 2 in s, so we do nothing.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>k == indices.length == sources.length == targets.length</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
	<li><code>0 &lt;= indexes[i] &lt; s.length</code></li>
	<li><code>1 &lt;= sources[i].length, targets[i].length &lt;= 50</code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>sources[i]</code> and <code>targets[i]</code> consist of only lowercase English letters.</li>
</ul>
</div>