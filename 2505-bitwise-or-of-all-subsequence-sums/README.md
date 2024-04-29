<h2><a href="https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/">2505. Bitwise OR of All Subsequence Sums</a></h2><h3>Medium</h3><hr><div><p>Given an integer array <code>nums</code>, return <em>the value of the bitwise </em><strong>OR</strong><em> of the sum of all possible <strong>subsequences</strong> in the array</em>.</p>

<p>A <strong>subsequence</strong> is a sequence that can be derived from another sequence by removing zero or more elements without changing the order of the remaining elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,1,0,3]
<strong>Output:</strong> 7
<strong>Explanation:</strong> All possible subsequence sums that we can have are: 0, 1, 2, 3, 4, 5, 6.
And we have 0 OR 1 OR 2 OR 3 OR 4 OR 5 OR 6 = 7, so we return 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,0,0]
<strong>Output:</strong> 0
<strong>Explanation:</strong> 0 is the only possible subsequence sum we can have, so we return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>