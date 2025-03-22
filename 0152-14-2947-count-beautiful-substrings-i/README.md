<h2> 152 14
2947. Count Beautiful Substrings I</h2><hr><div><p>You are given a string <code>s</code> and a positive integer <code>k</code>.</p>

<p>Let <code>vowels</code> and <code>consonants</code> be the number of vowels and consonants in a string.</p>

<p>A string is <strong>beautiful</strong> if:</p>

<ul>
	<li><code>vowels == consonants</code>.</li>
	<li><code>(vowels * consonants) % k == 0</code>, in other terms the multiplication of <code>vowels</code> and <code>consonants</code> is divisible by <code>k</code>.</li>
</ul>

<p>Return <em>the number of <strong>non-empty beautiful substrings</strong> in the given string</em> <code>s</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters in a string.</p>

<p><strong>Vowel letters</strong> in English are <code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, and <code>'u'</code>.</p>

<p><strong>Consonant letters</strong> in English are every letter except vowels.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "baeyh", k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 beautiful substrings in the given string.
- Substring "b<u>aeyh</u>", vowels = 2 (["a",e"]), consonants = 2 (["y","h"]).
You can see that string "aeyh" is beautiful as vowels == consonants and vowels * consonants % k == 0.
- Substring "<u>baey</u>h", vowels = 2 (["a",e"]), consonants = 2 (["b","y"]). 
You can see that string "baey" is beautiful as vowels == consonants and vowels * consonants % k == 0.
It can be shown that there are only 2 beautiful substrings in the given string.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "abba", k = 1
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are 3 beautiful substrings in the given string.
- Substring "<u>ab</u>ba", vowels = 1 (["a"]), consonants = 1 (["b"]). 
- Substring "ab<u>ba</u>", vowels = 1 (["a"]), consonants = 1 (["b"]).
- Substring "<u>abba</u>", vowels = 2 (["a","a"]), consonants = 2 (["b","b"]).
It can be shown that there are only 3 beautiful substrings in the given string.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "bcdf", k = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no beautiful substrings in the given string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 1000</code></li>
	<li><code>s</code> consists of only English lowercase letters.</li>
</ul>
</div>