<h2><a href="https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii">4119. Minimum Distance Between Three Equal Elements II</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code>.</p>

<p>A tuple <code>(i, j, k)</code> of 3 <strong>distinct</strong> indices is <strong>good</strong> if <code>nums[i] == nums[j] == nums[k]</code>.</p>

<p>The <strong>distance</strong> of a <strong>good</strong> tuple is <code>abs(i - j) + abs(j - k) + abs(k - i)</code>, where <code>abs(x)</code> denotes the <strong>absolute value</strong> of <code>x</code>.</p>

<p>Return an integer denoting the <strong>minimum</strong> possible <strong>distance</strong> of a <strong>good</strong> tuple. If no <strong>good</strong> tuples exist, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1,1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>The minimum distance is achieved by the good tuple <code>(0, 2, 3)</code>.</p>

<p><code>(0, 2, 3)</code> is a good tuple because <code>nums[0] == nums[2] == nums[3] == 1</code>. Its distance is <code>abs(0 - 2) + abs(2 - 3) + abs(3 - 0) = 2 + 1 + 3 = 6</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,2,3,2,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<p>The minimum distance is achieved by the good tuple <code>(2, 4, 6)</code>.</p>

<p><code>(2, 4, 6)</code> is a good tuple because <code>nums[2] == nums[4] == nums[6] == 2</code>. Its distance is <code>abs(2 - 4) + abs(4 - 6) + abs(6 - 2) = 2 + 2 + 4 = 8</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no good tuples. Therefore, the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= n</code></li>
</ul>
