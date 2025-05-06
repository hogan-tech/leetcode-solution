<h2><a href="https://leetcode.com/problems/find-the-longest-semi-repetitive-substring">2786. Find the Longest Semi-Repetitive Substring</a></h2><h3>Medium</h3><hr><p>You are given a digit string <code>s</code> that consists of digits from 0 to 9.</p>

<p>A string is called <strong>semi-repetitive</strong> if there is <strong>at most</strong> one adjacent pair of the same digit. For example, <code>&quot;0010&quot;</code>, <code>&quot;002020&quot;</code>, <code>&quot;0123&quot;</code>, <code>&quot;2002&quot;</code>, and <code>&quot;54944&quot;</code> are semi-repetitive while the following are not: <code>&quot;00101022&quot;</code> (adjacent same digit pairs are 00 and 22), and <code>&quot;1101234883&quot;</code> (adjacent same digit pairs are 11 and 88).</p>

<p>Return the length of the <strong>longest semi-repetitive <span data-keyword="substring-nonempty">substring</span></strong> of <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;52233&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest semi-repetitive substring is &quot;5223&quot;. Picking the whole string &quot;52233&quot; has two adjacent same digit pairs 22 and 33, but at most one is allowed.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;5494&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p><code>s</code> is a semi-repetitive string.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;1111111&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The longest semi-repetitive substring is &quot;11&quot;. Picking the substring &quot;111&quot; has two adjacent same digit pairs, but at most one is allowed.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>&#39;0&#39; &lt;= s[i] &lt;= &#39;9&#39;</code></li>
</ul>
