<h2><a href="https://leetcode.com/problems/minimum-subarrays-in-a-valid-split">2607. Minimum Subarrays in a Valid Split</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code>.</p>

<p>Splitting of an integer array <code>nums</code> into <strong>subarrays</strong> is <strong>valid</strong> if:</p>

<ul>
	<li>the <em>greatest common divisor</em> of the first and last elements of each subarray is <strong>greater</strong> than <code>1</code>, and</li>
	<li>each element of <code>nums</code> belongs to exactly one subarray.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> number of subarrays in a <strong>valid</strong> subarray splitting of</em> <code>nums</code>. If a valid subarray splitting is not possible, return <code>-1</code>.</p>

<p><strong>Note</strong> that:</p>

<ul>
	<li>The <strong>greatest common divisor</strong> of two numbers is the largest positive integer that evenly divides both numbers.</li>
	<li>A <strong>subarray</strong> is a contiguous non-empty part of an array.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,6,3,4,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can create a valid split in the following way: [2,6] | [3,4,3].
- The starting element of the 1<sup>st</sup> subarray is 2 and the ending is 6. Their greatest common divisor is 2, which is greater than 1.
- The starting element of the 2<sup>nd</sup> subarray is 3 and the ending is 3. Their greatest common divisor is 3, which is greater than 1.
It can be proved that 2 is the minimum number of subarrays that we can obtain in a valid split.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can create a valid split in the following way: [3] | [5].
- The starting element of the 1<sup>st</sup> subarray is 3 and the ending is 3. Their greatest common divisor is 3, which is greater than 1.
- The starting element of the 2<sup>nd</sup> subarray is 5 and the ending is 5. Their greatest common divisor is 5, which is greater than 1.
It can be proved that 2 is the minimum number of subarrays that we can obtain in a valid split.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It is impossible to create valid split.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
