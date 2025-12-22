<h2><a href="https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal">4138. Minimum Deletion Cost to Make All Characters Equal</a></h2><h3>Medium</h3><hr><p>You are given a string <code>s</code> of length <code>n</code> and an integer array <code>cost</code> of the same length, where <code>cost[i]</code> is the cost to <strong>delete</strong> the <code>i<sup>th</sup></code> character of <code>s</code>.</p>

<p>You may delete any number of characters from <code>s</code> (possibly none), such that the resulting string is <strong>non-empty</strong> and consists of <strong>equal</strong> characters.</p>

<p>Return an integer denoting the <strong>minimum</strong> total deletion cost required.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;aabaac&quot;, cost = [1,2,3,4,1,10]</span></p>

<p><strong>Output:</strong> <span class="example-io">11</span></p>

<p><strong>Explanation:</strong></p>

<p>Deleting the characters at indices 0, 1, 2, 3, 4 results in the string <code>&quot;c&quot;</code>, which consists of equal characters, and the total cost is <code>cost[0] + cost[1] + cost[2] + cost[3] + cost[4] = 1 + 2 + 3 + 4 + 1 = 11</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abc&quot;, cost = [10,5,8]</span></p>

<p><strong>Output:</strong> <span class="example-io">13</span></p>

<p><strong>Explanation:</strong></p>

<p>Deleting the characters at indices 1 and 2 results in the string <code>&quot;a&quot;</code>, which consists of equal characters, and the total cost is <code>cost[1] + cost[2] = 5 + 8 = 13</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;zzzzz&quot;, cost = [67,67,67,67,67]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>All characters in <code>s</code> are equal, so the deletion cost is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == s.length == cost.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= cost[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>
