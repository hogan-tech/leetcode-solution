<h2><a href="https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i">3143. Longest Unequal Adjacent Groups Subsequence I</a></h2><h3>Easy</h3><hr><p>You are given a string array <code>words</code> and a <strong>binary</strong> array <code>groups</code> both of length <code>n</code>, where <code>words[i]</code> is associated with <code>groups[i]</code>.</p>

<p>Your task is to select the <strong>longest alternating</strong> <span data-keyword="subsequence-array">subsequence</span> from <code>words</code>. A subsequence of <code>words</code> is alternating if for any two consecutive strings in the sequence, their corresponding elements in the binary array <code>groups</code> differ. Essentially, you are to choose strings such that adjacent elements have non-matching corresponding bits in the <code>groups</code> array.</p>

<p>Formally, you need to find the longest subsequence of an array of indices <code>[0, 1, ..., n - 1]</code> denoted as <code>[i<sub>0</sub>, i<sub>1</sub>, ..., i<sub>k-1</sub>]</code>, such that <code>groups[i<sub>j</sub>] != groups[i<sub>j+1</sub>]</code> for each <code>0 &lt;= j &lt; k - 1</code> and then find the words corresponding to these indices.</p>

<p>Return <em>the selected subsequence. If there are multiple answers, return <strong>any</strong> of them.</em></p>

<p><strong>Note:</strong> The elements in <code>words</code> are distinct.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">words = [&quot;e&quot;,&quot;a&quot;,&quot;b&quot;], groups = [0,0,1]</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">[&quot;e&quot;,&quot;b&quot;]</span></p>

<p><strong>Explanation:</strong> A subsequence that can be selected is <code>[&quot;e&quot;,&quot;b&quot;]</code> because <code>groups[0] != groups[2]</code>. Another subsequence that can be selected is <code>[&quot;a&quot;,&quot;b&quot;]</code> because <code>groups[1] != groups[2]</code>. It can be demonstrated that the length of the longest subsequence of indices that satisfies the condition is <code>2</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;
">
<p><strong>Input:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">words = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;,&quot;d&quot;], groups = [1,0,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;
">[&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]</span></p>

<p><strong>Explanation:</strong> A subsequence that can be selected is <code>[&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]</code> because <code>groups[0] != groups[1]</code> and <code>groups[1] != groups[2]</code>. Another subsequence that can be selected is <code>[&quot;a&quot;,&quot;b&quot;,&quot;d&quot;]</code> because <code>groups[0] != groups[1]</code> and <code>groups[1] != groups[3]</code>. It can be shown that the length of the longest subsequence of indices that satisfies the condition is <code>3</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == words.length == groups.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>groups[i]</code> is either <code>0</code> or <code>1.</code></li>
	<li><code>words</code> consists of <strong>distinct</strong> strings.</li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
</ul>
