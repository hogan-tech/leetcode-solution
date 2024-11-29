<h2><a href="https://leetcode.com/problems/find-smallest-letter-greater-than-target/">744. Find Smallest Letter Greater Than Target</a></h2><h3>Easy</h3><hr><div><p>You are given an array of characters <code>letters</code> that is sorted in <strong>non-decreasing order</strong>, and a character <code>target</code>. There are <strong>at least two different</strong> characters in <code>letters</code>.</p>

<p>Return <em>the smallest character in </em><code>letters</code><em> that is lexicographically greater than </em><code>target</code>. If such a character does not exist, return the first character in <code>letters</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> letters = ["c","f","j"], target = "a"
<strong>Output:</strong> "c"
<strong>Explanation:</strong> The smallest character that is lexicographically greater than 'a' in letters is 'c'.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> letters = ["c","f","j"], target = "c"
<strong>Output:</strong> "f"
<strong>Explanation:</strong> The smallest character that is lexicographically greater than 'c' in letters is 'f'.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> letters = ["x","x","y","y"], target = "z"
<strong>Output:</strong> "x"
<strong>Explanation:</strong> There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= letters.length &lt;= 10<sup>4</sup></code></li>
	<li><code>letters[i]</code> is a lowercase English letter.</li>
	<li><code>letters</code> is sorted in <strong>non-decreasing</strong> order.</li>
	<li><code>letters</code> contains at least two different characters.</li>
	<li><code>target</code> is a lowercase English letter.</li>
</ul>
</div>