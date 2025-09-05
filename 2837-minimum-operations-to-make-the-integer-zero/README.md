<h2><a href="https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero">2837. Minimum Operations to Make the Integer Zero</a></h2><h3>Medium</h3><hr><p>You are given two integers <code>num1</code> and <code>num2</code>.</p>

<p>In one operation, you can choose integer <code>i</code> in the range <code>[0, 60]</code> and subtract <code>2<sup>i</sup> + num2</code> from <code>num1</code>.</p>

<p>Return <em>the integer denoting the <strong>minimum</strong> number of operations needed to make</em> <code>num1</code> <em>equal to</em> <code>0</code>.</p>

<p>If it is impossible to make <code>num1</code> equal to <code>0</code>, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = 3, num2 = -2
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can make 3 equal to 0 with the following operations:
- We choose i = 2 and subtract 2<sup>2</sup> + (-2) from 3, 3 - (4 + (-2)) = 1.
- We choose i = 2 and subtract 2<sup>2</sup>&nbsp;+ (-2) from 1, 1 - (4 + (-2)) = -1.
- We choose i = 0 and subtract 2<sup>0</sup>&nbsp;+ (-2) from -1, (-1) - (1 + (-2)) = 0.
It can be proven, that 3 is the minimum number of operations that we need to perform.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = 5, num2 = 7
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be proven, that it is impossible to make 5 equal to 0 with the given operation.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num1 &lt;= 10<sup>9</sup></code></li>
	<li><code><font face="monospace">-10<sup>9</sup>&nbsp;&lt;= num2 &lt;= 10<sup>9</sup></font></code></li>
</ul>
