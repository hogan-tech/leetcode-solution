<h2><a href="https://leetcode.com/problems/generate-tag-for-video-caption">3893. Generate Tag for Video Caption</a></h2><h3>Easy</h3><hr><p>You are given a string <code><font face="monospace">caption</font></code> representing the caption for a video.</p>

<p>The following actions must be performed <strong>in order</strong> to generate a <strong>valid tag</strong> for the video:</p>

<ol>
	<li>
	<p><strong>Combine all words</strong> in the string into a single <em>camelCase string</em> prefixed with <code>&#39;#&#39;</code>. A <em>camelCase string</em> is one where the first letter of all words <em>except</em> the first one is capitalized. All characters after the first character in <strong>each</strong> word must be lowercase.</p>
	</li>
	<li>
	<p><b>Remove</b> all characters that are not an English letter, <strong>except</strong> the first <code>&#39;#&#39;</code>.</p>
	</li>
	<li>
	<p><strong>Truncate</strong> the result to a maximum of 100 characters.</p>
	</li>
</ol>

<p>Return the <strong>tag</strong> after performing the actions on <code>caption</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">caption = &quot;Leetcode daily streak achieved&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;#leetcodeDailyStreakAchieved&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>The first letter for all words except <code>&quot;leetcode&quot;</code> should be capitalized.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">caption = &quot;can I Go There&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;#canIGoThere&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>The first letter for all words except <code>&quot;can&quot;</code> should be capitalized.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">caption = &quot;hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Since the first word has length 101, we need to truncate the last two letters from the word.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= caption.length &lt;= 150</code></li>
	<li><code>caption</code> consists only of English letters and <code>&#39; &#39;</code>.</li>
</ul>
