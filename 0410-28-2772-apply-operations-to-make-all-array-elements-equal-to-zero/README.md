<h2> 410 28
2772. Apply Operations to Make All Array Elements Equal to Zero</h2><hr><div><p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> and a positive integer <code>k</code>.</p>

<p>You can apply the following operation on the array <strong>any</strong> number of times:</p>

<ul>
	<li>Choose <strong>any</strong> subarray of size <code>k</code> from the array and <strong>decrease</strong> all its elements by <code>1</code>.</li>
</ul>

<p>Return <code>true</code><em> if you can make all the array elements equal to </em><code>0</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>A <strong>subarray</strong> is a contiguous non-empty part of an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,2,3,1,1,0], k = 3
<strong>Output:</strong> true
<strong>Explanation:</strong> We can do the following operations:
- Choose the subarray [2,2,3]. The resulting array will be nums = [<strong><u>1</u></strong>,<strong><u>1</u></strong>,<strong><u>2</u></strong>,1,1,0].
- Choose the subarray [2,1,1]. The resulting array will be nums = [1,1,<strong><u>1</u></strong>,<strong><u>0</u></strong>,<strong><u>0</u></strong>,0].
- Choose the subarray [1,1,1]. The resulting array will be nums = [<u><strong>0</strong></u>,<u><strong>0</strong></u>,<u><strong>0</strong></u>,0,0,0].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,3,1,1], k = 2
<strong>Output:</strong> false
<strong>Explanation:</strong> It is not possible to make all the array elements equal to 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>
</div>