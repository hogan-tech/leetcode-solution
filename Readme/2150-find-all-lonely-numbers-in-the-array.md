<h2> 666 63
2150. Find All Lonely Numbers in the Array</h2><hr><div><p>You are given an integer array <code>nums</code>. A number <code>x</code> is <strong>lonely</strong> when it appears only <strong>once</strong>, and no <strong>adjacent</strong> numbers (i.e. <code>x + 1</code> and <code>x - 1)</code> appear in the array.</p>

<p>Return <em><strong>all</strong> lonely numbers in </em><code>nums</code>. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [10,6,5,8]
<strong>Output:</strong> [10,8]
<strong>Explanation:</strong> 
- 10 is a lonely number since it appears exactly once and 9 and 11 does not appear in nums.
- 8 is a lonely number since it appears exactly once and 7 and 9 does not appear in nums.
- 5 is not a lonely number since 6 appears in nums and vice versa.
Hence, the lonely numbers in nums are [10, 8].
Note that [8, 10] may also be returned.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,3,5,3]
<strong>Output:</strong> [1,5]
<strong>Explanation:</strong> 
- 1 is a lonely number since it appears exactly once and 0 and 2 does not appear in nums.
- 5 is a lonely number since it appears exactly once and 4 and 6 does not appear in nums.
- 3 is not a lonely number since it appears twice.
Hence, the lonely numbers in nums are [1, 5].
Note that [5, 1] may also be returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>
</div>