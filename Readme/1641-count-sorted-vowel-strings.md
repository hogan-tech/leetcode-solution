<h2><a href="https://leetcode.com/problems/count-sorted-vowel-strings">1761. Count Sorted Vowel Strings</a></h2><h3>Medium</h3><hr><p>Given an integer <code>n</code>, return <em>the number of strings of length </em><code>n</code><em> that consist only of vowels (</em><code>a</code><em>, </em><code>e</code><em>, </em><code>i</code><em>, </em><code>o</code><em>, </em><code>u</code><em>) and are <strong>lexicographically sorted</strong>.</em></p>

<p>A string <code>s</code> is <strong>lexicographically sorted</strong> if for all valid <code>i</code>, <code>s[i]</code> is the same as or comes before <code>s[i+1]</code> in the alphabet.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 5
<strong>Explanation:</strong> The 5 sorted strings that consist of vowels only are <code>[&quot;a&quot;,&quot;e&quot;,&quot;i&quot;,&quot;o&quot;,&quot;u&quot;].</code>
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 15
<strong>Explanation:</strong> The 15 sorted strings that consist of vowels only are
[&quot;aa&quot;,&quot;ae&quot;,&quot;ai&quot;,&quot;ao&quot;,&quot;au&quot;,&quot;ee&quot;,&quot;ei&quot;,&quot;eo&quot;,&quot;eu&quot;,&quot;ii&quot;,&quot;io&quot;,&quot;iu&quot;,&quot;oo&quot;,&quot;ou&quot;,&quot;uu&quot;].
Note that &quot;ea&quot; is not a valid string since &#39;e&#39; comes after &#39;a&#39; in the alphabet.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 33
<strong>Output:</strong> 66045
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 50</code>&nbsp;</li>
</ul>
