<h2><a href="https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array">1102. Check If a Number Is Majority Element in a Sorted Array</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code> sorted in non-decreasing order and an integer <code>target</code>, return <code>true</code> <em>if</em> <code>target</code> <em>is a <strong>majority</strong> element, or </em><code>false</code><em> otherwise</em>.</p>

<p>A <strong>majority</strong> element in an array <code>nums</code> is an element that appears more than <code>nums.length / 2</code> times in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,4,5,5,5,5,5,6,6], target = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 &gt; 9/2 is true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,100,101,101], target = 101
<strong>Output:</strong> false
<strong>Explanation:</strong> The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 &gt; 4/2 is false.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], target &lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> is sorted in non-decreasing order.</li>
</ul>
