<h2><a href="https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum">4085. Largest Prime from Consecutive Prime Sum</a></h2><h3>Medium</h3><hr><p>You are given an integer <code>n</code>.</p>

<p>Return the <strong>largest <span data-keyword="prime-number">prime number</span></strong> less than or equal to <code>n</code> that can be expressed as the <strong>sum</strong> of one or more <strong>consecutive prime numbers</strong> starting from 2. If no such number exists, return 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 20</span></p>

<p><strong>Output:</strong> <span class="example-io">17</span></p>

<p><strong>Explanation:</strong></p>

<p>The prime numbers less than or equal to <code>n = 20</code> which are consecutive prime sums are:</p>

<ul>
	<li>
	<p><code>2 = 2</code></p>
	</li>
	<li>
	<p><code>5 = 2 + 3</code></p>
	</li>
	<li>
	<p><code>17 = 2 + 3 + 5 + 7</code></p>
	</li>
</ul>

<p>The largest is 17, so it is the answer.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The only consecutive prime sum less than or equal to 2 is 2 itself.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>5</sup></code></li>
</ul>
