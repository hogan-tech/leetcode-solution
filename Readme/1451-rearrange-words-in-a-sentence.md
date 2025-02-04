<h2> 765 75
1451. Rearrange Words in a Sentence</h2><hr><div><p>Given a sentence&nbsp;<code>text</code> (A&nbsp;<em>sentence</em>&nbsp;is a string of space-separated words) in the following format:</p>

<ul>
	<li>First letter is in upper case.</li>
	<li>Each word in <code>text</code> are separated by a single space.</li>
</ul>

<p>Your task is to rearrange the words in text such that&nbsp;all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.</p>

<p>Return the new text&nbsp;following the format shown above.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> text = "Leetcode is cool"
<strong>Output:</strong> "Is cool leetcode"
<strong>Explanation: </strong>There are 3 words, "Leetcode" of length 8, "is" of length 2 and "cool" of length 4.
Output is ordered by length and the new first word starts with capital letter.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> text = "Keep calm and code on"
<strong>Output:</strong> "On and keep calm code"
<strong>Explanation: </strong>Output is ordered as follows:
"On" 2 letters.
"and" 3 letters.
"keep" 4 letters in case of tie order by position in original text.
"calm" 4 letters.
"code" 4 letters.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> text = "To be or not to be"
<strong>Output:</strong> "To be or to be not"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>text</code> begins with a capital letter and then contains lowercase letters and single space between words.</li>
	<li><code>1 &lt;= text.length &lt;= 10^5</code></li>
</ul>
</div>