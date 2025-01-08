<h2> 158 14
3042. Count Prefix and Suffix Pairs I</h2><hr><div><p>You are given a <strong>0-indexed</strong> string array <code>words</code>.</p>

<p>Let's define a <strong>boolean</strong> function <code>isPrefixAndSuffix</code> that takes two strings, <code>str1</code> and <code>str2</code>:</p>

<ul>
	<li><code>isPrefixAndSuffix(str1, str2)</code> returns <code>true</code> if <code>str1</code> is <strong>both</strong> a <span data-keyword="string-prefix">prefix</span> and a <span data-keyword="string-suffix">suffix</span> of <code>str2</code>, and <code>false</code> otherwise.</li>
</ul>

<p>For example, <code>isPrefixAndSuffix("aba", "ababa")</code> is <code>true</code> because <code>"aba"</code> is a prefix of <code>"ababa"</code> and also a suffix, but <code>isPrefixAndSuffix("abc", "abcd")</code> is <code>false</code>.</p>

<p>Return <em>an integer denoting the <strong>number</strong> of index pairs </em><code>(i, j)</code><em> such that </em><code>i &lt; j</code><em>, and </em><code>isPrefixAndSuffix(words[i], words[j])</code><em> is </em><code>true</code><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> words = ["a","aba","ababa","aa"]
<strong>Output:</strong> 4
<strong>Explanation:</strong> In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is true.
i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is true.
i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is true.
i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is true.
Therefore, the answer is 4.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> words = ["pa","papa","ma","mama"]
<strong>Output:</strong> 2
<strong>Explanation:</strong> In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("pa", "papa") is true.
i = 2 and j = 3 because isPrefixAndSuffix("ma", "mama") is true.
Therefore, the answer is 2.  </pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> words = ["abab","ab"]
<strong>Output:</strong> 0
<strong>Explanation: </strong>In this example, the only valid index pair is i = 0 and j = 1, and isPrefixAndSuffix("abab", "ab") is false.
Therefore, the answer is 0.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 50</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>words[i]</code> consists only of lowercase English letters.</li>
</ul>
</div>