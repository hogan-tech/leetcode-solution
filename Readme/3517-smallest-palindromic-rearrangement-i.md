<h2><a href="https://leetcode.com/problems/smallest-palindromic-rearrangement-i">3812. Smallest Palindromic Rearrangement I</a></h2><h3>Medium</h3><hr><p>You are given a <strong>palindromic</strong> string <code>s</code>.</p>

<p>Return the lexicographically <strong>smallest</strong> palindromic permutation of <code>s</code>.</p>

<p>A string is <strong>palindromic</strong> if it reads the same forward and backward.</p>

<p>A <strong>permutation</strong> is a rearrangement of all the characters of a string.</p>
A string <code>a</code> is <strong>lexicographically smaller</strong> than a string <code>b</code> if in the first position where <code>a</code> and <code>b</code> differ, string <code>a</code> has a letter that appears earlier in the alphabet than the corresponding letter in <code>b</code>.<br />
If the first <code>min(a.length, b.length)</code> characters do not differ, then the shorter string is the lexicographically smaller one.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;z&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;z&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>A string of only one character is already the lexicographically smallest palindrome.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;babab&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;abbba&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Rearranging <code>&quot;babab&quot;</code> &rarr; <code>&quot;abbba&quot;</code> gives the smallest lexicographic palindrome.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;daccad&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;acddca&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Rearranging <code>&quot;daccad&quot;</code> &rarr; <code>&quot;acddca&quot;</code> gives the smallest lexicographic palindrome.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>s</code> is guaranteed to be palindromic.</li>
</ul>
