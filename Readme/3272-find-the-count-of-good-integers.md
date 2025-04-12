<h2><a href="https://leetcode.com/problems/find-the-count-of-good-integers">3548. Find the Count of Good Integers</a></h2><h3>Hard</h3><hr><p>You are given two <strong>positive</strong> integers <code>n</code> and <code>k</code>.</p>

<p>An integer <code>x</code> is called <strong>k-palindromic</strong> if:</p>

<ul>
	<li><code>x</code> is a <span data-keyword="palindrome-integer">palindrome</span>.</li>
	<li><code>x</code> is divisible by <code>k</code>.</li>
</ul>

<p>An integer is called <strong>good</strong> if its digits can be <em>rearranged</em> to form a <strong>k-palindromic</strong> integer. For example, for <code>k = 2</code>, 2020 can be rearranged to form the <em>k-palindromic</em> integer 2002, whereas 1010 cannot be rearranged to form a <em>k-palindromic</em> integer.</p>

<p>Return the count of <strong>good</strong> integers containing <code>n</code> digits.</p>

<p><strong>Note</strong> that <em>any</em> integer must <strong>not</strong> have leading zeros, <strong>neither</strong> before <strong>nor</strong> after rearrangement. For example, 1010 <em>cannot</em> be rearranged to form 101.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, k = 5</span></p>

<p><strong>Output:</strong> <span class="example-io">27</span></p>

<p><strong>Explanation:</strong></p>

<p><em>Some</em> of the good integers are:</p>

<ul>
	<li>551 because it can be rearranged to form 515.</li>
	<li>525 because it is already k-palindromic.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 1, k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The two good integers are 4 and 8.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, k = 6</span></p>

<p><strong>Output:</strong> <span class="example-io">2468</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>1 &lt;= k &lt;= 9</code></li>
</ul>
