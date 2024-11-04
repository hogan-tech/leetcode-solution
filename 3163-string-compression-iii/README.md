<h2><a href="https://leetcode.com/problems/string-compression-iii/">3163. String Compression III</a></h2><h3>Medium</h3><hr><div><p>Given a string <code>word</code>, compress it using the following algorithm:</p>

<ul>
	<li>Begin with an empty string <code>comp</code>. While <code>word</code> is <strong>not</strong> empty, use the following operation:

	<ul>
		<li>Remove a maximum length prefix of <code>word</code> made of a <em>single character</em> <code>c</code> repeating <strong>at most</strong> 9 times.</li>
		<li>Append the length of the prefix followed by <code>c</code> to <code>comp</code>.</li>
	</ul>
	</li>
</ul>

<p>Return the string <code>comp</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = "abcde"</span></p>

<p><strong>Output:</strong> <span class="example-io">"1a1b1c1d1e"</span></p>

<p><strong>Explanation:</strong></p>

<p>Initially, <code>comp = ""</code>. Apply the operation 5 times, choosing <code>"a"</code>, <code>"b"</code>, <code>"c"</code>, <code>"d"</code>, and <code>"e"</code> as the prefix in each operation.</p>

<p>For each prefix, append <code>"1"</code> followed by the character to <code>comp</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = "aaaaaaaaaaaaaabb"</span></p>

<p><strong>Output:</strong> <span class="example-io">"9a5a2b"</span></p>

<p><strong>Explanation:</strong></p>

<p>Initially, <code>comp = ""</code>. Apply the operation 3 times, choosing <code>"aaaaaaaaa"</code>, <code>"aaaaa"</code>, and <code>"bb"</code> as the prefix in each operation.</p>

<ul>
	<li>For prefix <code>"aaaaaaaaa"</code>, append <code>"9"</code> followed by <code>"a"</code> to <code>comp</code>.</li>
	<li>For prefix <code>"aaaaa"</code>, append <code>"5"</code> followed by <code>"a"</code> to <code>comp</code>.</li>
	<li>For prefix <code>"bb"</code>, append <code>"2"</code> followed by <code>"b"</code> to <code>comp</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>word</code> consists only of lowercase English letters.</li>
</ul>
</div>