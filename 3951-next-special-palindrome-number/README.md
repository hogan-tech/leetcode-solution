<h2><a href="https://leetcode.com/problems/next-special-palindrome-number">3951. Next Special Palindrome Number</a></h2><h3>Hard</h3><hr><p>You are given an integer <code>n</code>.</p>

<p>A number is called <strong>special</strong> if:</p>

<ul>
	<li>It is a <strong><span data-keyword="palindrome-integer">palindrome</span></strong>.</li>
	<li>Every digit <code>k</code> in the number appears <strong>exactly</strong> <code>k</code> times.</li>
</ul>

<p>Return the <strong>smallest</strong> special number <strong>strictly </strong>greater than <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">22</span></p>

<p><strong>Explanation:</strong></p>

<p>22 is the smallest special number greater than 2, as it is a palindrome and the digit 2 appears exactly 2 times.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 33</span></p>

<p><strong>Output:</strong> <span class="example-io">212</span></p>

<p><strong>Explanation:</strong></p>

<p>212 is the smallest special number greater than 33, as it is a palindrome and the digits 1 and 2 appear exactly 1 and 2 times respectively.<br />
 </p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>15</sup></code></li>
</ul>
