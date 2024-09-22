<h2><a href="https://leetcode.com/problems/report-spam-message/">3295. Report Spam Message</a></h2><h3>Medium</h3><hr><div><p>You are given an array of strings <code>message</code> and an array of strings <code>bannedWords</code>.</p>

<p>An array of words is considered <strong>spam</strong> if there are <strong>at least</strong> two words in it that <b>exactly</b> match any word in <code>bannedWords</code>.</p>

<p>Return <code>true</code> if the array <code>message</code> is spam, and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">message = ["hello","world","leetcode"], bannedWords = ["world","hello"]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p>The words <code>"hello"</code> and <code>"world"</code> from the <code>message</code> array both appear in the <code>bannedWords</code> array.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>Only one word from the <code>message</code> array (<code>"programming"</code>) appears in the <code>bannedWords</code> array.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= message.length, bannedWords.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= message[i].length, bannedWords[i].length &lt;= 15</code></li>
	<li><code>message[i]</code> and <code>bannedWords[i]</code> consist only of lowercase English letters.</li>
</ul>
</div>