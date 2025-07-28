<h2><a href="https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting">3948. Maximum Number of Subsequences After One Inserting</a></h2><h3>Medium</h3><hr><p>You are given a string <code>s</code> consisting of uppercase English letters.</p>

<p>You are allowed to insert <strong>at most one</strong> uppercase English letter at <strong>any</strong> position (including the beginning or end) of the string.</p>

<p>Return the <strong>maximum</strong> number of <code>&quot;LCT&quot;</code> <span data-keyword="subsequence-string-nonempty">subsequences</span> that can be formed in the resulting string after <strong>at most one insertion</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;LMCT&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>We can insert a <code>&quot;L&quot;</code> at the beginning of the string s to make <code>&quot;LLMCT&quot;</code>, which has 2 subsequences, at indices [0, 3, 4] and [1, 3, 4].</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;LCCT&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>We can insert a <code>&quot;L&quot;</code> at the beginning of the string s to make <code>&quot;LLCCT&quot;</code>, which has 4 subsequences, at indices [0, 2, 4], [0, 3, 4], [1, 2, 4] and [1, 3, 4].</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;L&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>Since it is not possible to obtain the subsequence <code>&quot;LCT&quot;</code> by inserting a single letter, the result is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of uppercase English letters.</li>
</ul>
