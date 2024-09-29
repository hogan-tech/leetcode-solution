<h2><a href="https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/">3304. Find the K-th Character in String Game I</a></h2><h3>Easy</h3><hr><div><p>Alice and Bob are playing a game. Initially, Alice has a string <code>word = "a"</code>.</p>

<p>You are given a <strong>positive</strong> integer <code>k</code>.</p>

<p>Now Bob will ask Alice to perform the following operation <strong>forever</strong>:</p>

<ul>
	<li>Generate a new string by <strong>changing</strong> each character in <code>word</code> to its <strong>next</strong> character in the English alphabet, and <strong>append</strong> it to the <em>original</em> <code>word</code>.</li>
</ul>

<p>For example, performing the operation on <code>"c"</code> generates <code>"cd"</code> and performing the operation on <code>"zb"</code> generates <code>"zbac"</code>.</p>

<p>Return the value of the <code>k<sup>th</sup></code> character in <code>word</code>, after enough operations have been done for <code>word</code> to have <strong>at least</strong> <code>k</code> characters.</p>

<p><strong>Note</strong> that the character <code>'z'</code> can be changed to <code>'a'</code> in the operation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">k = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">"b"</span></p>

<p><strong>Explanation:</strong></p>

<p>Initially, <code>word = "a"</code>. We need to do the operation three times:</p>

<ul>
	<li>Generated string is <code>"b"</code>, <code>word</code> becomes <code>"ab"</code>.</li>
	<li>Generated string is <code>"bc"</code>, <code>word</code> becomes <code>"abbc"</code>.</li>
	<li>Generated string is <code>"bccd"</code>, <code>word</code> becomes <code>"abbcbccd"</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">k = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">"c"</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 500</code></li>
</ul>
</div>