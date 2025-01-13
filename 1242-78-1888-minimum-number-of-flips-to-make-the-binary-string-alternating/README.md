<h2> 1242 78
1888. Minimum Number of Flips to Make the Binary String Alternating</h2><hr><div><p>You are given a binary string <code>s</code>. You are allowed to perform two types of operations on the string in any sequence:</p>

<ul>
	<li><strong>Type-1: Remove</strong> the character at the start of the string <code>s</code> and <strong>append</strong> it to the end of the string.</li>
	<li><strong>Type-2: Pick</strong> any character in <code>s</code> and <strong>flip</strong> its value, i.e., if its value is <code>'0'</code> it becomes <code>'1'</code> and vice-versa.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> number of <strong>type-2</strong> operations you need to perform</em> <em>such that </em><code>s</code> <em>becomes <strong>alternating</strong>.</em></p>

<p>The string is called <strong>alternating</strong> if no two adjacent characters are equal.</p>

<ul>
	<li>For example, the strings <code>"010"</code> and <code>"1010"</code> are alternating, while the string <code>"0100"</code> is not.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "111000"
<strong>Output:</strong> 2
<strong>Explanation</strong>: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "10<u>1</u>01<u>0</u>".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "010"
<strong>Output:</strong> 0
<strong>Explanation</strong>: The string is already alternating.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "1110"
<strong>Output:</strong> 1
<strong>Explanation</strong>: Use the second operation on the second element to make s = "1<u>0</u>10".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>'0'</code> or <code>'1'</code>.</li>
</ul>
</div>