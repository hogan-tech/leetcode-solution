<h2><a href="https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k">4068. Sum of Elements With Frequency Divisible by K</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>Return an integer denoting the <strong>sum</strong> of all elements in <code>nums</code> whose <strong><span data-keyword="frequency-array">frequency</span></strong> is divisible by <code>k</code>, or 0 if there are no such elements.</p>

<p><strong>Note:</strong> An element is included in the sum <strong>exactly</strong> as many times as it appears in the array if its total frequency is divisible by <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2,3,3,3,3,4], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">16</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The number 1 appears once (odd frequency).</li>
	<li>The number 2 appears twice (even frequency).</li>
	<li>The number 3 appears four times (even frequency).</li>
	<li>The number 4 appears once (odd frequency).</li>
</ul>

<p>So, the total sum is <code>2 + 2 + 3 + 3 + 3 + 3 = 16</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,5], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no elements that appear an even number of times, so the total sum is 0.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,4,4,1,2,3], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The number 1 appears once.</li>
	<li>The number 2 appears once.</li>
	<li>The number 3 appears once.</li>
	<li>The number 4 appears three times.</li>
</ul>

<p>So, the total sum is <code>4 + 4 + 4 = 12</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>
