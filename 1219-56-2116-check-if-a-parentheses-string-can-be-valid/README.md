<h2> 1219 56
2116. Check if a Parentheses String Can Be Valid</h2><hr><div><p>A parentheses string is a <strong>non-empty</strong> string consisting only of <code>'('</code> and <code>')'</code>. It is valid if <strong>any</strong> of the following conditions is <strong>true</strong>:</p>

<ul>
	<li>It is <code>()</code>.</li>
	<li>It can be written as <code>AB</code> (<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid parentheses strings.</li>
	<li>It can be written as <code>(A)</code>, where <code>A</code> is a valid parentheses string.</li>
</ul>

<p>You are given a parentheses string <code>s</code> and a string <code>locked</code>, both of length <code>n</code>. <code>locked</code> is a binary string consisting only of <code>'0'</code>s and <code>'1'</code>s. For <strong>each</strong> index <code>i</code> of <code>locked</code>,</p>

<ul>
	<li>If <code>locked[i]</code> is <code>'1'</code>, you <strong>cannot</strong> change <code>s[i]</code>.</li>
	<li>But if <code>locked[i]</code> is <code>'0'</code>, you <strong>can</strong> change <code>s[i]</code> to either <code>'('</code> or <code>')'</code>.</li>
</ul>

<p>Return <code>true</code> <em>if you can make <code>s</code> a valid parentheses string</em>. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/06/eg1.png" style="width: 311px; height: 101px;">
<pre><strong>Input:</strong> s = "))()))", locked = "010100"
<strong>Output:</strong> true
<strong>Explanation:</strong> locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "()()", locked = "0000"
<strong>Output:</strong> true
<strong>Explanation:</strong> We do not need to make any changes because s is already valid.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = ")", locked = "0"
<strong>Output:</strong> false
<strong>Explanation:</strong> locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == s.length == locked.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>'('</code> or <code>')'</code>.</li>
	<li><code>locked[i]</code> is either <code>'0'</code> or <code>'1'</code>.</li>
</ul>
</div>