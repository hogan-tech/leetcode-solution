<h2> 1 0
3427. Sum of Variable Length Subarrays</h2><hr><div><p>You are given an integer array <code>nums</code> of size <code>n</code>. For <strong>each</strong> index <code>i</code> where <code>0 &lt;= i &lt; n</code>, define a subarray <code>nums[start ... i]</code> where <code>start = max(0, i - nums[i])</code>.</p>

<p>Return the total sum of all elements from the subarray defined for each index in the array.</p>
A <strong>subarray</strong> is a contiguous <b>non-empty</b> sequence of elements within an array.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">11</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Sum</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>nums[0] = [2]</code></td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>nums[0 ... 1] = [2, 3]</code></td>
			<td style="border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>nums[1 ... 2] = [3, 1]</code></td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><strong>Total Sum</strong></td>
			<td style="border: 1px solid black;">&nbsp;</td>
			<td style="border: 1px solid black;">11</td>
		</tr>
	</tbody>
</table>

<p>The total sum is 11. Hence, 11 is the output.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,1,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">13</span></p>

<p><strong>Explanation:</strong></p>

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">i</th>
			<th style="border: 1px solid black;">Subarray</th>
			<th style="border: 1px solid black;">Sum</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;"><code>nums[0] = [3]</code></td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;"><code>nums[0 ... 1] = [3, 1]</code></td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;"><code>nums[1 ... 2] = [1, 1]</code></td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;"><code>nums[1 ... 3] = [1, 1, 2]</code></td>
			<td style="border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;"><strong>Total Sum</strong></td>
			<td style="border: 1px solid black;">&nbsp;</td>
			<td style="border: 1px solid black;">13</td>
		</tr>
	</tbody>
</table>

<p>The total sum is 13. Hence, 13 is the output.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>
</div>