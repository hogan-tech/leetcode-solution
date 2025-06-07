<h2><a href="https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars">3445. Lexicographically Minimum String After Removing Stars</a></h2><h3>Medium</h3><hr><p>You are given a string <code>s</code>. It may contain any number of <code>&#39;*&#39;</code> characters. Your task is to remove all <code>&#39;*&#39;</code> characters.</p>

<p>While there is a <code>&#39;*&#39;</code>, do the following operation:</p>

<ul>
	<li>Delete the leftmost <code>&#39;*&#39;</code> and the <strong>smallest</strong> non-<code>&#39;*&#39;</code> character to its <em>left</em>. If there are several smallest characters, you can delete any of them.</li>
</ul>

<p>Return the <span data-keyword="lexicographically-smaller-string">lexicographically smallest</span> resulting string after removing all <code>&#39;*&#39;</code> characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aaba*&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;aab&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>We should delete one of the <code>&#39;a&#39;</code> characters with <code>&#39;*&#39;</code>. If we choose <code>s[3]</code>, <code>s</code> becomes the lexicographically smallest.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;abc&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no <code>&#39;*&#39;</code> in the string.<!-- notionvc: ff07e34f-b1d6-41fb-9f83-5d0ba3c1ecde --></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters and <code>&#39;*&#39;</code>.</li>
	<li>The input is generated such that it is possible to delete all <code>&#39;*&#39;</code> characters.</li>
</ul>
