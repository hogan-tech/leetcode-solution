<h2> 652 37
2295. Replace Elements in an Array</h2><hr><div><p>You are given a <strong>0-indexed</strong> array <code>nums</code> that consists of <code>n</code> <strong>distinct</strong> positive integers. Apply <code>m</code> operations to this array, where in the <code>i<sup>th</sup></code> operation you replace the number <code>operations[i][0]</code> with <code>operations[i][1]</code>.</p>

<p>It is guaranteed that in the <code>i<sup>th</sup></code> operation:</p>

<ul>
	<li><code>operations[i][0]</code> <strong>exists</strong> in <code>nums</code>.</li>
	<li><code>operations[i][1]</code> does <strong>not</strong> exist in <code>nums</code>.</li>
</ul>

<p>Return <em>the array obtained after applying all the operations</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]
<strong>Output:</strong> [3,2,7,1]
<strong>Explanation:</strong> We perform the following operations on nums:
- Replace the number 1 with 3. nums becomes [<u><strong>3</strong></u>,2,4,6].
- Replace the number 4 with 7. nums becomes [3,2,<u><strong>7</strong></u>,6].
- Replace the number 6 with 1. nums becomes [3,2,7,<u><strong>1</strong></u>].
We return the final array [3,2,7,1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2], operations = [[1,3],[2,1],[3,2]]
<strong>Output:</strong> [2,1]
<strong>Explanation:</strong> We perform the following operations to nums:
- Replace the number 1 with 3. nums becomes [<u><strong>3</strong></u>,2].
- Replace the number 2 with 1. nums becomes [3,<u><strong>1</strong></u>].
- Replace the number 3 with 2. nums becomes [<u><strong>2</strong></u>,1].
We return the array [2,1].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>m == operations.length</code></li>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
	<li>All the values of <code>nums</code> are <strong>distinct</strong>.</li>
	<li><code>operations[i].length == 2</code></li>
	<li><code>1 &lt;= nums[i], operations[i][0], operations[i][1] &lt;= 10<sup>6</sup></code></li>
	<li><code>operations[i][0]</code> will exist in <code>nums</code> when applying the <code>i<sup>th</sup></code> operation.</li>
	<li><code>operations[i][1]</code> will not exist in <code>nums</code> when applying the <code>i<sup>th</sup></code> operation.</li>
</ul>
</div>