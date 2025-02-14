<h2> 580 64
3066. Minimum Operations to Exceed Threshold Value II</h2><hr><div><p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>, and an integer <code>k</code>.</p>

<p>You are allowed to perform some operations on <code>nums</code>, where in a single operation, you can:</p>

<ul>
	<li>Select the two <strong>smallest</strong> integers <code>x</code> and <code>y</code> from <code>nums</code>.</li>
	<li>Remove <code>x</code> and <code>y</code> from <code>nums</code>.</li>
	<li>Insert <code>(min(x, y) * 2 + max(x, y))</code> at any position in the array.</li>
</ul>

<p><strong>Note</strong> that you can only apply the described operation if <code>nums</code> contains <strong>at least</strong> two elements.</p>

<p>Return the <strong>minimum</strong> number of operations needed so that all elements of the array are <strong>greater than or equal to</strong> <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,11,10,1,3], k = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ol>
	<li>In the first operation, we remove elements 1 and 2, then add <code>1 * 2 + 2</code> to <code>nums</code>. <code>nums</code> becomes equal to <code>[4, 11, 10, 3]</code>.</li>
	<li>In the second operation, we remove elements 3 and 4, then add <code>3 * 2 + 4</code> to <code>nums</code>. <code>nums</code> becomes equal to <code>[10, 11, 10]</code>.</li>
</ol>

<p>At this stage, all the elements of nums are greater than or equal to 10 so we can stop.&nbsp;</p>

<p>It can be shown that 2 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,2,4,9], k = 20</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ol>
	<li>After one operation, <code>nums</code> becomes equal to <code>[2, 4, 9, 3]</code>.&nbsp;</li>
	<li>After two operations, <code>nums</code> becomes equal to <code>[7, 4, 9]</code>.&nbsp;</li>
	<li>After three operations, <code>nums</code> becomes equal to <code>[15, 9]</code>.&nbsp;</li>
	<li>After four operations, <code>nums</code> becomes equal to <code>[33]</code>.</li>
</ol>

<p>At this stage, all the elements of <code>nums</code> are greater than 20 so we can stop.&nbsp;</p>

<p>It can be shown that 4 is the minimum number of operations needed so that all elements of the array are greater than or equal to 20.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
	<li>The input is generated such that an answer always exists. That is, there exists some sequence of operations after which all elements of the array are greater than or equal to <code>k</code>.</li>
</ul>
</div>