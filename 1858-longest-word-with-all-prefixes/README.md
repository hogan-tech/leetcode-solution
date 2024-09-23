<h2><a href="https://leetcode.com/problems/longest-word-with-all-prefixes/">1858. Longest Word With All Prefixes</a></h2><h3>Medium</h3><hr><div><p>Given an array of strings <code>words</code>, find the <strong>longest</strong> string in <code>words</code> such that <strong>every prefix</strong> of it is also in <code>words</code>.</p>

<ul>
	<li>For example, let <code>words = ["a", "app", "ap"]</code>. The string <code>"app"</code> has prefixes <code>"ap"</code> and <code>"a"</code>, all of which are in <code>words</code>.</li>
</ul>

<p>Return <em>the string described above. If there is more than one string with the same length, return the <strong>lexicographically smallest</strong> one, and if no string exists, return </em><code>""</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["k","ki","kir","kira", "kiran"]
<strong>Output:</strong> "kiran"
<strong>Explanation:</strong> "kiran" has prefixes "kira", "kir", "ki", and "k", and all of them appear in words.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
<strong>Output:</strong> "apple"
<strong>Explanation:</strong> Both "apple" and "apply" have all their prefixes in words.
However, "apple" is lexicographically smaller, so we return that.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> words = ["abc", "bc", "ab", "qwe"]
<strong>Output:</strong> ""
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= sum(words[i].length) &lt;= 10<sup>5</sup></code></li>
</ul></div>