<h2><a href="https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters">395. Longest Substring with At Least K Repeating Characters</a></h2><h3>Medium</h3><hr><p>Given a string <code>s</code> and an integer <code>k</code>, return <em>the length of the longest substring of</em> <code>s</code> <em>such that the frequency of each character in this substring is greater than or equal to</em> <code>k</code>.</p>

<p data-pm-slice="1 1 []">if no such substring exists, return 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aaabb&quot;, k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The longest substring is &quot;aaa&quot;, as &#39;a&#39; is repeated 3 times.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ababbc&quot;, k = 2
<strong>Output:</strong> 5
<strong>Explanation:</strong> The longest substring is &quot;ababb&quot;, as &#39;a&#39; is repeated 2 times and &#39;b&#39; is repeated 3 times.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>
