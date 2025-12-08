<h2><a href="https://leetcode.com/problems/sort-integers-by-binary-reflection">4150. Sort Integers by Binary Reflection</a></h2><h3>Easy</h3><hr><p>You are given an integer array <code>nums</code>.</p>

<p>The <strong>binary reflection</strong> of a <strong>positive</strong> integer is defined as the number obtained by reversing the order of its <strong>binary</strong> digits (ignoring any leading zeros) and interpreting the resulting binary number as a decimal.</p>

<p>Sort the array in <strong>ascending</strong> order based on the binary reflection of each element. If two different numbers have the same binary reflection, the <strong>smaller</strong> original number should appear first.</p>

<p>Return the resulting sorted array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,5,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">[4,4,5]</span></p>

<p><strong>Explanation:</strong></p>

<p>Binary reflections are:</p>

<ul>
	<li>4 -&gt; (binary) <code>100</code> -&gt; (reversed) <code>001</code> -&gt; 1</li>
	<li>5 -&gt; (binary) <code>101</code> -&gt; (reversed) <code>101</code> -&gt; 5</li>
	<li>4 -&gt; (binary) <code>100</code> -&gt; (reversed) <code>001</code> -&gt; 1</li>
</ul>
Sorting by the reflected values gives <code>[4, 4, 5]</code>.</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,6,5,8]</span></p>

<p><strong>Output:</strong> <span class="example-io">[8,3,6,5]</span></p>

<p><strong>Explanation:</strong></p>

<p>Binary reflections are:</p>

<ul>
	<li>3 -&gt; (binary) <code>11</code> -&gt; (reversed) <code>11</code> -&gt; 3</li>
	<li>6 -&gt; (binary) <code>110</code> -&gt; (reversed) <code>011</code> -&gt; 3</li>
	<li>5 -&gt; (binary) <code>101</code> -&gt; (reversed) <code>101</code> -&gt; 5</li>
	<li>8 -&gt; (binary) <code>1000</code> -&gt; (reversed) <code>0001</code> -&gt; 1</li>
</ul>
Sorting by the reflected values gives <code>[8, 3, 6, 5]</code>.<br />
Note that 3 and 6 have the same reflection, so we arrange them in increasing order of original value.</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
