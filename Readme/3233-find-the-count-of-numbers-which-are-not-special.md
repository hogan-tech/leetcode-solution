<h2><a href="https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special">3507. Find the Count of Numbers Which Are Not Special</a></h2><h3>Medium</h3><hr><p>You are given 2 <strong>positive</strong> integers <code>l</code> and <code>r</code>. For any number <code>x</code>, all positive divisors of <code>x</code> <em>except</em> <code>x</code> are called the <strong>proper divisors</strong> of <code>x</code>.</p>

<p>A number is called <strong>special</strong> if it has exactly 2 <strong>proper divisors</strong>. For example:</p>

<ul>
	<li>The number 4 is <em>special</em> because it has proper divisors 1 and 2.</li>
	<li>The number 6 is <em>not special</em> because it has proper divisors 1, 2, and 3.</li>
</ul>

<p>Return the count of numbers in the range <code>[l, r]</code> that are <strong>not</strong> <strong>special</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">l = 5, r = 7</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no special numbers in the range <code>[5, 7]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">l = 4, r = 16</span></p>

<p><strong>Output:</strong> <span class="example-io">11</span></p>

<p><strong>Explanation:</strong></p>

<p>The special numbers in the range <code>[4, 16]</code> are 4 and 9.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= l &lt;= r &lt;= 10<sup>9</sup></code></li>
</ul>
