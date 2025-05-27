<h2><a href="https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string">2309. Maximize Number of Subsequences in a String</a></h2><h3>Medium</h3><hr><p>You are given a <strong>0-indexed</strong> string <code>text</code> and another <strong>0-indexed</strong> string <code>pattern</code> of length <code>2</code>, both of which consist of only lowercase English letters.</p>

<p>You can add <strong>either</strong> <code>pattern[0]</code> <strong>or</strong> <code>pattern[1]</code> anywhere in <code>text</code> <strong>exactly once</strong>. Note that the character can be added even at the beginning or at the end of <code>text</code>.</p>

<p>Return <em>the <strong>maximum</strong> number of times</em> <code>pattern</code> <em>can occur as a <strong>subsequence</strong> of the modified </em><code>text</code>.</p>

<p>A <b>subsequence</b> is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> text = &quot;abdcdbc&quot;, pattern = &quot;ac&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong>
If we add pattern[0] = &#39;a&#39; in between text[1] and text[2], we get &quot;ab<u><strong>a</strong></u>dcdbc&quot;. Now, the number of times &quot;ac&quot; occurs as a subsequence is 4.
Some other strings which have 4 subsequences &quot;ac&quot; after adding a character to text are &quot;<u><strong>a</strong></u>abdcdbc&quot; and &quot;abd<u><strong>a</strong></u>cdbc&quot;.
However, strings such as &quot;abdc<u><strong>a</strong></u>dbc&quot;, &quot;abd<u><strong>c</strong></u>cdbc&quot;, and &quot;abdcdbc<u><strong>c</strong></u>&quot;, although obtainable, have only 3 subsequences &quot;ac&quot; and are thus suboptimal.
It can be shown that it is not possible to get more than 4 subsequences &quot;ac&quot; by adding only one character.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> text = &quot;aabb&quot;, pattern = &quot;ab&quot;
<strong>Output:</strong> 6
<strong>Explanation:</strong>
Some of the strings which can be obtained from text and have 6 subsequences &quot;ab&quot; are &quot;<u><strong>a</strong></u>aabb&quot;, &quot;aa<u><strong>a</strong></u>bb&quot;, and &quot;aab<u><strong>b</strong></u>b&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 10<sup>5</sup></code></li>
	<li><code>pattern.length == 2</code></li>
	<li><code>text</code> and <code>pattern</code> consist only of lowercase English letters.</li>
</ul>
