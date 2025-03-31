<h2> 42 2
3503. Longest Palindrome After Substring Concatenation I</h2><hr><div><p>You are given two strings, <code>s</code> and <code>t</code>.</p>

<p>You can create a new string by selecting a <span data-keyword="substring">substring</span> from <code>s</code> (possibly empty) and a substring from <code>t</code> (possibly empty), then concatenating them <strong>in order</strong>.</p>

<p>Return the length of the <strong>longest</strong> <span data-keyword="palindrome-string">palindrome</span> that can be formed this way.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "a", t = "a"</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Concatenating <code>"a"</code> from <code>s</code> and <code>"a"</code> from <code>t</code> results in <code>"aa"</code>, which is a palindrome of length 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "abc", t = "def"</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Since all characters are different, the longest palindrome is any single character, so the answer is 1.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "b", t = "aaaa"</span></p>

<p><strong>Output:</strong> 4</p>

<p><strong>Explanation:</strong></p>

<p>Selecting "<code>aaaa</code>" from <code>t</code> is the longest palindrome, so the answer is 4.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "abcde", t = "ecdba"</span></p>

<p><strong>Output:</strong> 5</p>

<p><strong>Explanation:</strong></p>

<p>Concatenating <code>"abc"</code> from <code>s</code> and <code>"ba"</code> from <code>t</code> results in <code>"abcba"</code>, which is a palindrome of length 5.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 30</code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>
</div>