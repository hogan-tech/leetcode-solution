<h2> 490 12
2521. Distinct Prime Factors of Product of Array</h2><hr><div><p>Given an array of positive integers <code>nums</code>, return <em>the number of <strong>distinct prime factors</strong> in the product of the elements of</em> <code>nums</code>.</p>

<p><strong>Note</strong> that:</p>

<ul>
	<li>A number greater than <code>1</code> is called <strong>prime</strong> if it is divisible by only <code>1</code> and itself.</li>
	<li>An integer <code>val1</code> is a factor of another integer <code>val2</code> if <code>val2 / val1</code> is an integer.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,4,3,7,10,6]
<strong>Output:</strong> 4
<strong>Explanation:</strong>
The product of all the elements in nums is: 2 * 4 * 3 * 7 * 10 * 6 = 10080 = 2<sup>5</sup> * 3<sup>2</sup> * 5 * 7.
There are 4 distinct prime factors so we return 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [2,4,8,16]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
The product of all the elements in nums is: 2 * 4 * 8 * 16 = 1024 = 2<sup>10</sup>.
There is 1 distinct prime factor so we return 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>2 &lt;= nums[i] &lt;= 1000</code></li>
</ul>
</div>