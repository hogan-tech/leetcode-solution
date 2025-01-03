<h2> 32 72
2539. Count the Number of Good Subsequences</h2><hr><div><p>A <strong>subsequence</strong> of a string is&nbsp;good if it is not empty and the frequency of each one of its characters is the same.</p>

<p>Given a string <code>s</code>, return <em>the number of good subsequences of</em> <code>s</code>. Since the answer may be too large, return it modulo <code>10<sup>9</sup> + 7</code>.</p>

<p>A <strong>subsequence</strong> is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "aabb"
<strong>Output:</strong> 11
<strong>Explanation:</strong> The total number of subsequences is <code>2<sup>4</sup>. </code>There are five subsequences which are not good: "<strong><u>aab</u></strong>b", "a<u><strong>abb</strong></u>", "<strong><u>a</u></strong>a<u><strong>bb</strong></u>", "<u><strong>aa</strong></u>b<strong><u>b</u></strong>", and the empty subsequence. Hence, the number of good subsequences is <code>2<sup>4</sup>-5 = 11</code>.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "leet"
<strong>Output:</strong> 12
<strong>Explanation:</strong> There are four subsequences which are not good: "<strong><u>l</u><em>ee</em></strong>t", "l<u><strong>eet</strong></u>", "<strong><u>leet</u></strong>", and the empty subsequence. Hence, the number of good subsequences is <code>2<sup>4</sup>-4 = 12</code>.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "abcd"
<strong>Output:</strong> 15
<strong>Explanation:</strong> All of the non-empty subsequences are good subsequences. Hence, the number of good subsequences is <code>2<sup>4</sup>-1 = 15</code>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>
</div>