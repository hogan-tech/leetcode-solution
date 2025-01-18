<h2> 22 6
3424. Minimum Cost to Make Arrays Identical</h2><hr><div><p>You are given two integer arrays <code>arr</code> and <code>brr</code> of length <code>n</code>, and an integer <code>k</code>. You can perform the following operations on <code>arr</code> <em>any</em> number of times:</p>

<ul>
	<li>Split <code>arr</code> into <em>any</em> number of <strong>contiguous</strong> subarrays and rearrange these subarrays in <em>any order</em>. This operation has a fixed cost of <code>k</code>.</li>
	<li>
	<p>Choose any element in <code>arr</code> and add or subtract a positive integer <code>x</code> to it. The cost of this operation is <code>x</code>.</p>
	</li>
</ul>

<p>Return the <strong>minimum </strong>total cost to make <code>arr</code> <strong>equal</strong> to <code>brr</code>.</p>

<p>A <strong>subarray</strong> is a contiguous <b>non-empty</b> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">arr = [-7,9,5], brr = [7,-2,-5], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">13</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Split <code>arr</code> into two contiguous subarrays: <code>[-7]</code> and <code>[9, 5]</code> and rearrange them as <code>[9, 5, -7]</code>, with a cost of 2.</li>
	<li>Subtract 2 from element <code>arr[0]</code>. The array becomes <code>[7, 5, -7]</code>. The cost of this operation is 2.</li>
	<li>Subtract 7 from element <code>arr[1]</code>. The array becomes <code>[7, -2, -7]</code>. The cost of this operation is 7.</li>
	<li>Add 2 to element <code>arr[2]</code>. The array becomes <code>[7, -2, -5]</code>. The cost of this operation is 2.</li>
</ul>

<p>The total cost to make the arrays equal is <code>2 + 2 + 7 + 2 = 13</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">arr = [2,1], brr = [2,1], k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>Since the arrays are already equal, no operations are needed, and the total cost is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length == brr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= 2 * 10<sup>10</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= brr[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</div>