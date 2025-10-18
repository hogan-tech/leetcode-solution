<h2><a href="https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations">3620. Maximum Number of Distinct Elements After Operations</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>You are allowed to perform the following <strong>operation</strong> on each element of the array <strong>at most</strong> <em>once</em>:</p>

<ul>
	<li>Add an integer in the range <code>[-k, k]</code> to the element.</li>
</ul>

<p>Return the <strong>maximum</strong> possible number of <strong>distinct</strong> elements in <code>nums</code> after performing the <strong>operations</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,2,3,3,4], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p><code>nums</code> changes to <code>[-1, 0, 1, 2, 3, 4]</code> after performing operations on the first four elements.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,4,4,4], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>By adding -1 to <code>nums[0]</code> and 1 to <code>nums[1]</code>, <code>nums</code> changes to <code>[3, 5, 4, 4]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>
