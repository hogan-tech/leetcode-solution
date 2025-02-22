<h2> 258 189
2734. Lexicographically Smallest String After Substring Operation</h2><hr><div><p>Given a string <code>s</code> consisting of lowercase English letters. Perform the following operation:</p>

<ul>
	<li>Select any non-empty <span data-keyword="substring-nonempty">substring</span> then replace every letter of the substring with the preceding letter of the English alphabet. For example, 'b' is converted to 'a', and 'a' is converted to 'z'.</li>
</ul>

<p>Return the <span data-keyword="lexicographically-smaller-string"><strong>lexicographically smallest</strong></span> string <strong>after performing the operation</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "cbabc"</span></p>

<p><strong>Output:</strong> <span class="example-io">"baabc"</span></p>

<p><strong>Explanation:</strong></p>

<p>Perform the operation on the substring starting at index 0, and ending at index 1 inclusive.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "aa"</span></p>

<p><strong>Output:</strong> <span class="example-io">"az"</span></p>

<p><strong>Explanation:</strong></p>

<p>Perform the operation on the last letter.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "acbbc"</span></p>

<p><strong>Output:</strong> <span class="example-io">"abaab"</span></p>

<p><strong>Explanation:</strong></p>

<p>Perform the operation on the substring starting at index 1, and ending at index 4 inclusive.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "leetcode"</span></p>

<p><strong>Output:</strong> <span class="example-io">"kddsbncd"</span></p>

<p><strong>Explanation:</strong></p>

<p>Perform the operation on the entire string.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters</li>
</ul>
</div>