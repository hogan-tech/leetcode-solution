<h2><a href="https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/">2516. Take K of Each Character From Left and Right</a></h2><h3>Medium</h3><hr><div><p>You are given a string <code>s</code> consisting of the characters <code>'a'</code>, <code>'b'</code>, and <code>'c'</code> and a non-negative integer <code>k</code>. Each minute, you may take either the <strong>leftmost</strong> character of <code>s</code>, or the <strong>rightmost</strong> character of <code>s</code>.</p>

<p>Return<em> the <strong>minimum</strong> number of minutes needed for you to take <strong>at least</strong> </em><code>k</code><em> of each character, or return </em><code>-1</code><em> if it is not possible to take </em><code>k</code><em> of each character.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "aabaaaacaabc", k = 2
<strong>Output:</strong> 8
<strong>Explanation:</strong> 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "a", k = 1
<strong>Output:</strong> -1
<strong>Explanation:</strong> It is not possible to take one 'b' or 'c' so return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only the letters <code>'a'</code>, <code>'b'</code>, and <code>'c'</code>.</li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
</ul>
</div>