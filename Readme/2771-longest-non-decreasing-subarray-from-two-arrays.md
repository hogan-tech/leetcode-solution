<h2><a href="https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/">2771. Longest Non-decreasing Subarray From Two Arrays</a></h2><h3>Medium</h3><hr><div><p>You are given two <strong>0-indexed</strong> integer arrays <code>nums1</code> and <code>nums2</code> of length <code>n</code>.</p>

<p>Let's define another <strong>0-indexed</strong> integer array, <code>nums3</code>, of length <code>n</code>. For each index <code>i</code> in the range <code>[0, n - 1]</code>, you can assign either <code>nums1[i]</code> or <code>nums2[i]</code> to <code>nums3[i]</code>.</p>

<p>Your task is to maximize the length of the <strong>longest non-decreasing subarray</strong> in <code>nums3</code> by choosing its values optimally.</p>

<p>Return <em>an integer representing the length of the <strong>longest non-decreasing</strong> subarray in</em> <code>nums3</code>.</p>

<p><strong>Note: </strong>A <strong>subarray</strong> is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums1 = [2,3,1], nums2 = [1,2,1]
<strong>Output:</strong> 2
<strong>Explanation: </strong>One way to construct nums3 is: 
nums3 = [nums1[0], nums2[1], nums2[2]] =&gt; [2,2,1]. 
The subarray starting from index 0 and ending at index 1, [2,2], forms a non-decreasing subarray of length 2. 
We can show that 2 is the maximum achievable length.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums1 = [1,3,2,1], nums2 = [2,2,3,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong> One way to construct nums3 is: 
nums3 = [nums1[0], nums2[1], nums2[2], nums2[3]] =&gt; [1,2,3,4]. 
The entire array forms a non-decreasing subarray of length 4, making it the maximum achievable length.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums1 = [1,1], nums2 = [2,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong> One way to construct nums3 is: 
nums3 = [nums1[0], nums1[1]] =&gt; [1,1]. 
The entire array forms a non-decreasing subarray of length 2, making it the maximum achievable length.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length == nums2.length == n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>