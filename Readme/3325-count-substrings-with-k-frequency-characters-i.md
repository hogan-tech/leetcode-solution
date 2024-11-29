<h2><a href="https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/">3325. Count Substrings With K-Frequency Characters I</a></h2><h3>Medium</h3><hr><div><p>Given a string <code>s</code> and an integer <code>k</code>, return the total number of substrings of <code>s</code> where <strong>at least one</strong> character appears <strong>at least</strong> <code>k</code> times.</p>

<p>A <strong>substring</strong> is a contiguous <b>non-empty</b> sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "abacb", k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The valid substrings are:</p>

<ul>
	<li><code>"aba"</code> (character <code>'a'</code> appears 2 times).</li>
	<li><code>"abac"</code> (character <code>'a'</code> appears 2 times).</li>
	<li><code>"abacb"</code> (character <code>'a'</code> appears 2 times).</li>
	<li><code>"bacb"</code> (character <code>'b'</code> appears 2 times).</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "abcde", k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<p>All substrings are valid because every character appears at least once.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3000</code></li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>
</div>