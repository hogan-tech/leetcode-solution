<h2><a href="https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index">2855. Maximum Number of Jumps to Reach the Last Index</a></h2><h3>Medium</h3><hr><p>You are given a <strong>0-indexed</strong> array <code>nums</code> of <code>n</code> integers and an integer <code>target</code>.</p>

<p>You are initially positioned at index <code>0</code>. In one step, you can jump from index <code>i</code> to any index <code>j</code> such that:</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; n</code></li>
	<li><code>-target &lt;= nums[j] - nums[i] &lt;= target</code></li>
</ul>

<p>Return <em>the <strong>maximum number of jumps</strong> you can make to reach index</em> <code>n - 1</code>.</p>

<p>If there is no way to reach index <code>n - 1</code>, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,6,4,1,2], target = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
- Jump from index 0 to index 1. 
- Jump from index 1 to index 3.
- Jump from index 3 to index 5.
It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 3 jumps. Hence, the answer is 3. </pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,6,4,1,2], target = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> To go from index 0 to index n - 1 with the maximum number of jumps, you can perform the following jumping sequence:
- Jump from index 0 to index 1.
- Jump from index 1 to index 2.
- Jump from index 2 to index 3.
- Jump from index 3 to index 4.
- Jump from index 4 to index 5.
It can be proven that there is no other jumping sequence that goes from 0 to n - 1 with more than 5 jumps. Hence, the answer is 5. </pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,6,4,1,2], target = 0
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be proven that there is no jumping sequence that goes from 0 to n - 1. Hence, the answer is -1. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length == n &lt;= 1000</code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= target &lt;= 2 * 10<sup>9</sup></code></li>
</ul>
