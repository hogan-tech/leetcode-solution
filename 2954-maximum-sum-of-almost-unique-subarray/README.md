<h2><a href="https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray">2954. Maximum Sum of Almost Unique Subarray</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code> and two positive integers <code>m</code> and <code>k</code>.</p>

<p>Return <em>the <strong>maximum sum</strong> out of all <strong>almost unique</strong> subarrays of length </em><code>k</code><em> of</em> <code>nums</code>. If no such subarray exists, return <code>0</code>.</p>

<p>A subarray of <code>nums</code> is <strong>almost unique</strong> if it contains at least <code>m</code> distinct elements.</p>

<p>A subarray is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,6,7,3,1,7], m = 3, k = 4
<strong>Output:</strong> 18
<strong>Explanation:</strong> There are 3 almost unique subarrays of size <code>k = 4</code>. These subarrays are [2, 6, 7, 3], [6, 7, 3, 1], and [7, 3, 1, 7]. Among these subarrays, the one with the maximum sum is [2, 6, 7, 3] which has a sum of 18.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,9,9,2,4,5,4], m = 1, k = 3
<strong>Output:</strong> 23
<strong>Explanation:</strong> There are 5 almost unique subarrays of size k. These subarrays are [5, 9, 9], [9, 9, 2], [9, 2, 4], [2, 4, 5], and [4, 5, 4]. Among these subarrays, the one with the maximum sum is [5, 9, 9] which has a sum of 23.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1,2,1,2,1], m = 3, k = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no subarrays of size <code>k = 3</code> that contain at least <code>m = 3</code> distinct elements in the given array [1,2,1,2,1,2,1]. Therefore, no almost unique subarrays exist, and the maximum sum is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m &lt;= k &lt;= nums.length</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
