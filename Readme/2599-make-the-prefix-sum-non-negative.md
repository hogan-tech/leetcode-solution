<h2> 65 2
2599. Make the Prefix Sum Non-negative</h2><hr><div><p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>. You can apply the following operation any number of times:</p>

<ul>
	<li>Pick any element from <code>nums</code> and put it at the end of <code>nums</code>.</li>
</ul>

<p>The prefix sum array of <code>nums</code> is an array <code>prefix</code> of the same length as <code>nums</code> such that <code>prefix[i]</code> is the sum of all the integers <code>nums[j]</code> where <code>j</code> is in the inclusive range <code>[0, i]</code>.</p>

<p>Return <em>the minimum number of operations such that the prefix sum array does not contain negative integers</em>. The test cases are generated such that it is always possible to make the prefix sum array non-negative.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,3,-5,4]
<strong>Output:</strong> 0
<strong>Explanation:</strong> we do not need to do any operations.
The array is [2,3,-5,4]. The prefix sum array is [2, 5, 0, 4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [3,-5,-2,6]
<strong>Output:</strong> 1
<strong>Explanation:</strong> we can do one operation on index 1.
The array after the operation is [3,-2,6,-5]. The prefix sum array is [3, 1, 7, 2].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>