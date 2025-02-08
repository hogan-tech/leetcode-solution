<h2> 295 49
2587. Rearrange Array to Maximize Prefix Score</h2><hr><div><p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>. You can rearrange the elements of <code>nums</code> to <strong>any order</strong> (including the given order).</p>

<p>Let <code>prefix</code> be the array containing the prefix sums of <code>nums</code> after rearranging it. In other words, <code>prefix[i]</code> is the sum of the elements from <code>0</code> to <code>i</code> in <code>nums</code> after rearranging it. The <strong>score</strong> of <code>nums</code> is the number of positive integers in the array <code>prefix</code>.</p>

<p>Return <em>the maximum score you can achieve</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,-1,0,1,-3,3,-3]
<strong>Output:</strong> 6
<strong>Explanation:</strong> We can rearrange the array into nums = [2,3,1,-1,-3,0,-3].
prefix = [2,5,6,5,2,2,-1], so the score is 6.
It can be shown that 6 is the maximum score we can obtain.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [-2,-3,0]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Any rearrangement of the array will result in a score of 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>
</div>