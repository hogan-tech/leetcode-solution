<h2> 181 23
2957. Remove Adjacent Almost-Equal Characters</h2><hr><div><p>You are given a <strong>0-indexed</strong> string <code>word</code>.</p>

<p>In one operation, you can pick any index <code>i</code> of <code>word</code> and change <code>word[i]</code> to any lowercase English letter.</p>

<p>Return <em>the <strong>minimum</strong> number of operations needed to remove all adjacent <strong>almost-equal</strong> characters from</em> <code>word</code>.</p>

<p>Two characters <code>a</code> and <code>b</code> are <strong>almost-equal</strong> if <code>a == b</code> or <code>a</code> and <code>b</code> are adjacent in the alphabet.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> word = "aaaaa"
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can change word into "a<strong><u>c</u></strong>a<u><strong>c</strong></u>a" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> word = "abddez"
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can change word into "<strong><u>y</u></strong>bd<u><strong>o</strong></u>ez" which does not have any adjacent almost-equal characters.
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> word = "zyxyxyz"
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can change word into "z<u><strong>a</strong></u>x<u><strong>a</strong></u>x<strong><u>a</u></strong>z" which does not have any adjacent almost-equal characters. 
It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 100</code></li>
	<li><code>word</code> consists only of lowercase English letters.</li>
</ul>
</div>