<h2><a href="https://leetcode.com/problems/minimum-additions-to-make-valid-string">2736. Minimum Additions to Make Valid String</a></h2><h3>Medium</h3><hr><p>Given a string <code>word</code> to which you can insert letters &quot;a&quot;, &quot;b&quot; or &quot;c&quot; anywhere and any number of times, return <em>the minimum number of letters that must be inserted so that <code>word</code> becomes <strong>valid</strong>.</em></p>

<p>A string is called <strong>valid </strong>if it can be formed by concatenating the string &quot;abc&quot; several times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;b&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> Insert the letter &quot;a&quot; right before &quot;b&quot;, and the letter &quot;c&quot; right next to &quot;b&quot; to obtain the valid string &quot;<strong>a</strong>b<strong>c</strong>&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;aaa&quot;
<strong>Output:</strong> 6
<strong>Explanation:</strong> Insert letters &quot;b&quot; and &quot;c&quot; next to each &quot;a&quot; to obtain the valid string &quot;a<strong>bc</strong>a<strong>bc</strong>a<strong>bc</strong>&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> word = &quot;abc&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> word is already valid. No modifications are needed. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 50</code></li>
	<li><code>word</code> consists of letters &quot;a&quot;, &quot;b&quot;&nbsp;and &quot;c&quot; only.&nbsp;</li>
</ul>
