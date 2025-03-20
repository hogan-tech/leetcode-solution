<h2> 952 138
1375. Number of Times Binary String Is Prefix-Aligned</h2><hr><div><p>You have a <strong>1-indexed</strong> binary string of length <code>n</code> where all the bits are <code>0</code> initially. We will flip all the bits of this binary string (i.e., change them from <code>0</code> to <code>1</code>) one by one. You are given a <strong>1-indexed</strong> integer array <code>flips</code> where <code>flips[i]</code> indicates that the bit at index <code>i</code> will be flipped in the <code>i<sup>th</sup></code> step.</p>

<p>A binary string is <strong>prefix-aligned</strong> if, after the <code>i<sup>th</sup></code> step, all the bits in the <strong>inclusive</strong> range <code>[1, i]</code> are ones and all the other bits are zeros.</p>

<p>Return <em>the number of times the binary string is <strong>prefix-aligned</strong> during the flipping process</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> flips = [3,2,4,1,5]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The binary string is initially "00000".
After applying step 1: The string becomes "00100", which is not prefix-aligned.
After applying step 2: The string becomes "01100", which is not prefix-aligned.
After applying step 3: The string becomes "01110", which is not prefix-aligned.
After applying step 4: The string becomes "11110", which is prefix-aligned.
After applying step 5: The string becomes "11111", which is prefix-aligned.
We can see that the string was prefix-aligned 2 times, so we return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> flips = [4,1,2,3]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The binary string is initially "0000".
After applying step 1: The string becomes "0001", which is not prefix-aligned.
After applying step 2: The string becomes "1001", which is not prefix-aligned.
After applying step 3: The string becomes "1101", which is not prefix-aligned.
After applying step 4: The string becomes "1111", which is prefix-aligned.
We can see that the string was prefix-aligned 1 time, so we return 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == flips.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>flips</code> is a permutation of the integers in the range <code>[1, n]</code>.</li>
</ul>
</div>