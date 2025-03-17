<h2> 832 39
2206. Divide Array Into Equal Pairs</h2><hr><div><p>You are given an integer array <code>nums</code> consisting of <code>2 * n</code> integers.</p>

<p>You need to divide <code>nums</code> into <code>n</code> pairs such that:</p>

<ul>
	<li>Each element belongs to <strong>exactly one</strong> pair.</li>
	<li>The elements present in a pair are <strong>equal</strong>.</li>
</ul>

<p>Return <code>true</code> <em>if nums can be divided into</em> <code>n</code> <em>pairs, otherwise return</em> <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,2,3,2,2,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums.length == 2 * n</code></li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 500</code></li>
</ul>
</div>