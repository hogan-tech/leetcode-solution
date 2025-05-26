<h2><a href="https://leetcode.com/problems/find-xor-beauty-of-array">2621. Find Xor-Beauty of Array</a></h2><h3>Medium</h3><hr><p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>.</p>

<p>The <strong>effective value</strong> of three indices <code>i</code>, <code>j</code>, and <code>k</code> is defined as <code>((nums[i] | nums[j]) &amp; nums[k])</code>.</p>

<p>The <strong>xor-beauty</strong> of the array is the XORing of <strong>the effective values of all the possible triplets</strong> of indices <code>(i, j, k)</code> where <code>0 &lt;= i, j, k &lt; n</code>.</p>

<p>Return <em>the xor-beauty of</em> <code>nums</code>.</p>

<p><strong>Note</strong> that:</p>

<ul>
	<li><code>val1 | val2</code> is bitwise OR of <code>val1</code> and <code>val2</code>.</li>
	<li><code>val1 &amp; val2</code> is bitwise AND of <code>val1</code> and <code>val2</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
The triplets and their corresponding effective values are listed below:
- (0,0,0) with effective value ((1 | 1) &amp; 1) = 1
- (0,0,1) with effective value ((1 | 1) &amp; 4) = 0
- (0,1,0) with effective value ((1 | 4) &amp; 1) = 1
- (0,1,1) with effective value ((1 | 4) &amp; 4) = 4
- (1,0,0) with effective value ((4 | 1) &amp; 1) = 1
- (1,0,1) with effective value ((4 | 1) &amp; 4) = 4
- (1,1,0) with effective value ((4 | 4) &amp; 1) = 0
- (1,1,1) with effective value ((4 | 4) &amp; 4) = 4 
Xor-beauty of array will be bitwise XOR of all beauties = 1 ^ 0 ^ 1 ^ 4 ^ 1 ^ 4 ^ 0 ^ 4 = 5.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [15,45,20,2,34,35,5,44,32,30]
<strong>Output:</strong> 34
<strong>Explanation:</strong> <code>The xor-beauty of the given array is 34.</code>
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
