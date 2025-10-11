<h2><a href="https://leetcode.com/problems/equal-score-substrings">4052. Equal Score Substrings</a></h2><h3>Easy</h3><hr><p>You are given a string <code>s</code> consisting of lowercase English letters.</p>

<p>The <strong>score</strong> of a string is the sum of the positions of its characters in the alphabet, where <code>&#39;a&#39; = 1</code>, <code>&#39;b&#39; = 2</code>, ..., <code>&#39;z&#39; = 26</code>.</p>

<p>Determine whether there exists an index <code>i</code> such that the string can be split into two <strong>non-empty substrings</strong> <code>s[0..i]</code> and <code>s[(i + 1)..(n - 1)]</code> that have <strong>equal</strong> scores.</p>

<p>Return <code>true</code> if such a split exists, otherwise return <code>false</code>.</p>
A <strong>substring</strong> is a contiguous <b>non-empty</b> sequence of characters within a string.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;adcb&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>Split at index <code>i = 1</code>:</p>

<ul>
	<li>Left substring = <code>s[0..1] = &quot;ad&quot;</code> with <code>score = 1 + 4 = 5</code></li>
	<li>Right substring = <code>s[2..3] = &quot;cb&quot;</code> with <code>score = 3 + 2 = 5</code></li>
</ul>

<p>Both substrings have equal scores, so the output is <code>true</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;bace&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:​​​​​​</strong></p>

<p><strong>​​​​​​​</strong>No split produces equal scores, so the output is <code>false</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>
