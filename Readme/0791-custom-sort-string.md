<h2><a href="https://leetcode.com/problems/custom-sort-string/">791. Custom Sort String</a></h2><h3>Medium</h3><hr><div><p>You are given two strings <code>order</code> and <code>s</code>. All the characters of <code>order</code> are <strong>unique</strong> and were sorted in some custom order previously.</p>

<p>Permute the characters of <code>s</code> so that they match the order that <code>order</code> was sorted. More specifically, if a character <code>x</code> occurs before a character <code>y</code> in <code>order</code>, then <code>x</code> should occur before <code>y</code> in the permuted string.</p>

<p>Return <em>any permutation of </em><code>s</code><em> that satisfies this property</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1: </strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> order = "cba", s = "abcd" </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> "cbad" </span></p>

<p><strong>Explanation: </strong> <code>"a"</code>, <code>"b"</code>, <code>"c"</code> appear in order, so the order of <code>"a"</code>, <code>"b"</code>, <code>"c"</code> should be <code>"c"</code>, <code>"b"</code>, and <code>"a"</code>.</p>

<p>Since <code>"d"</code> does not appear in <code>order</code>, it can be at any position in the returned string. <code>"dcba"</code>, <code>"cdba"</code>, <code>"cbda"</code> are also valid outputs.</p>
</div>

<p><strong class="example">Example 2: </strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> order = "bcafg", s = "abcd" </span></p>

<p><strong>Output: </strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> "bcad" </span></p>

<p><strong>Explanation: </strong> The characters <code>"b"</code>, <code>"c"</code>, and <code>"a"</code> from <code>order</code> dictate the order for the characters in <code>s</code>. The character <code>"d"</code> in <code>s</code> does not appear in <code>order</code>, so its position is flexible.</p>

<p>Following the order of appearance in <code>order</code>, <code>"b"</code>, <code>"c"</code>, and <code>"a"</code> from <code>s</code> should be arranged as <code>"b"</code>, <code>"c"</code>, <code>"a"</code>. <code>"d"</code> can be placed at any position since it's not in order. The output <code>"bcad"</code> correctly follows this rule. Other arrangements like <code>"bacd"</code> or <code>"bcda"</code> would also be valid, as long as <code>"b"</code>, <code>"c"</code>, <code>"a"</code> maintain their order.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= order.length &lt;= 26</code></li>
	<li><code>1 &lt;= s.length &lt;= 200</code></li>
	<li><code>order</code> and <code>s</code> consist of lowercase English letters.</li>
	<li>All the characters of <code>order</code> are <strong>unique</strong>.</li>
</ul>
</div>