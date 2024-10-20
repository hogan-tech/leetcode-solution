<h2><a href="https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/">3324. Find the Sequence of Strings Appeared on the Screen</a></h2><h3>Medium</h3><hr><div><p>You are given a string <code>target</code>.</p>

<p>Alice is going to type <code>target</code> on her computer using a special keyboard that has <strong>only two</strong> keys:</p>

<ul>
	<li>Key 1 appends the character <code>"a"</code> to the string on the screen.</li>
	<li>Key 2 changes the <strong>last</strong> character of the string on the screen to its <strong>next</strong> character in the English alphabet. For example, <code>"c"</code> changes to <code>"d"</code> and <code>"z"</code> changes to <code>"a"</code>.</li>
</ul>

<p><strong>Note</strong> that initially there is an <em>empty</em> string <code>""</code> on the screen, so she can <strong>only</strong> press key 1.</p>

<p>Return a list of <em>all</em> strings that appear on the screen as Alice types <code>target</code>, in the order they appear, using the <strong>minimum</strong> key presses.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">target = "abc"</span></p>

<p><strong>Output:</strong> <span class="example-io">["a","aa","ab","aba","abb","abc"]</span></p>

<p><strong>Explanation:</strong></p>

<p>The sequence of key presses done by Alice are:</p>

<ul>
	<li>Press key 1, and the string on the screen becomes <code>"a"</code>.</li>
	<li>Press key 1, and the string on the screen becomes <code>"aa"</code>.</li>
	<li>Press key 2, and the string on the screen becomes <code>"ab"</code>.</li>
	<li>Press key 1, and the string on the screen becomes <code>"aba"</code>.</li>
	<li>Press key 2, and the string on the screen becomes <code>"abb"</code>.</li>
	<li>Press key 2, and the string on the screen becomes <code>"abc"</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">target = "he"</span></p>

<p><strong>Output:</strong> <span class="example-io">["a","b","c","d","e","f","g","h","ha","hb","hc","hd","he"]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 400</code></li>
	<li><code>target</code> consists only of lowercase English letters.</li>
</ul>
</div>