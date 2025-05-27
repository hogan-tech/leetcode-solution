<h2><a href="https://leetcode.com/problems/sum-of-numbers-with-units-digit-k">1334. Sum of Numbers With Units Digit K</a></h2><h3>Medium</h3><hr><p>Given two integers <code>num</code> and <code>k</code>, consider a set of positive integers with the following properties:</p>

<ul>
	<li>The units digit of each integer is <code>k</code>.</li>
	<li>The sum of the integers is <code>num</code>.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> possible size of such a set, or </em><code>-1</code><em> if no such set exists.</em></p>

<p>Note:</p>

<ul>
	<li>The set can contain multiple instances of the same integer, and the sum of an empty set is considered <code>0</code>.</li>
	<li>The <strong>units digit</strong> of a number is the rightmost digit of the number.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 58, k = 9
<strong>Output:</strong> 2
<strong>Explanation:</strong>
One valid set is [9,49], as the sum is 58 and each integer has a units digit of 9.
Another valid set is [19,39].
It can be shown that 2 is the minimum possible size of a valid set.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 37, k = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> It is not possible to obtain a sum of 37 using only integers that have a units digit of 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = 0, k = 7
<strong>Output:</strong> 0
<strong>Explanation:</strong> The sum of an empty set is considered 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 3000</code></li>
	<li><code>0 &lt;= k &lt;= 9</code></li>
</ul>
