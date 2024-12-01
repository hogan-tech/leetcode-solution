<h2><a href="https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/">3371. Identify the Largest Outlier in an Array</a></h2><h3>Medium</h3><hr><div><p>You are given an integer array <code>nums</code>. This array contains <code>n</code> elements, where <strong>exactly</strong> <code>n - 2</code> elements are <strong>special</strong><strong> numbers</strong>. One of the remaining <strong>two</strong> elements is the <em>sum</em> of these <strong>special numbers</strong>, and the other is an <strong>outlier</strong>.</p>

<p>An <strong>outlier</strong> is defined as a number that is <em>neither</em> one of the original special numbers <em>nor</em> the element representing the sum of those numbers.</p>

<p><strong>Note</strong> that special numbers, the sum element, and the outlier must have <strong>distinct</strong> indices, but <em>may </em>share the <strong>same</strong> value.</p>

<p>Return the <strong>largest</strong><strong> </strong>potential<strong> outlier</strong> in <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,5,10]</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<p>The special numbers could be 2 and 3, thus making their sum 5 and the outlier 10.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-2,-1,-3,-6,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The special numbers could be -2, -1, and -3, thus making their sum -6 and the outlier 4.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1,1,1,5,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The special numbers could be 1, 1, 1, 1, and 1, thus making their sum 5 and the other 5 as the outlier.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li>The input is generated such that at least <strong>one</strong> potential outlier exists in <code>nums</code>.</li>
</ul>
</div>