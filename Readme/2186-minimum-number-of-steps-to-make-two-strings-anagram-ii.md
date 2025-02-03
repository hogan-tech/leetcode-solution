<h2> 583 26
2186. Minimum Number of Steps to Make Two Strings Anagram II</h2><hr><div><p>You are given two strings <code>s</code> and <code>t</code>. In one step, you can append <strong>any character</strong> to either <code>s</code> or <code>t</code>.</p>

<p>Return <em>the minimum number of steps to make </em><code>s</code><em> and </em><code>t</code><em> <strong>anagrams</strong> of each other.</em></p>

<p>An <strong>anagram</strong> of a string is a string that contains the same characters with a different (or the same) ordering.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "<strong><u>lee</u></strong>tco<u><strong>de</strong></u>", t = "co<u><strong>a</strong></u>t<u><strong>s</strong></u>"
<strong>Output:</strong> 7
<strong>Explanation:</strong> 
- In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcode<strong><u>as</u></strong>".
- In 5 steps, we can append the letters in "leede" onto t = "coats", forming t = "coats<u><strong>leede</strong></u>".
"leetcodeas" and "coatsleede" are now anagrams of each other.
We used a total of 2 + 5 = 7 steps.
It can be shown that there is no way to make them anagrams of each other with less than 7 steps.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "night", t = "thing"
<strong>Output:</strong> 0
<strong>Explanation:</strong> The given strings are already anagrams of each other. Thus, we do not need any further steps.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>
</div>