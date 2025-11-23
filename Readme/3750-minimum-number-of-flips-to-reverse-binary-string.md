<h2><a href="https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string">4126. Minimum Number of Flips to Reverse Binary String</a></h2><h3>Easy</h3><hr><p>You are given a <strong>positive</strong> integer <code>n</code>.</p>

<p>Let <code>s</code> be the <strong>binary representation</strong> of <code>n</code> without leading zeros.</p>

<p>The <strong>reverse</strong> of a binary string <code>s</code> is obtained by writing the characters of <code>s</code> in the opposite order.</p>

<p>You may flip any bit in <code>s</code> (change <code>0 &rarr; 1</code> or <code>1 &rarr; 0</code>). Each flip affects <strong>exactly</strong> one bit.</p>

<p>Return the <strong>minimum</strong> number of flips required to make <code>s</code> equal to the reverse of its original form.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 7</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The binary representation of 7 is <code>&quot;111&quot;</code>. Its reverse is also <code>&quot;111&quot;</code>, which is the same. Hence, no flips are needed.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The binary representation of 10 is <code>&quot;1010&quot;</code>. Its reverse is <code>&quot;0101&quot;</code>. All four bits must be flipped to make them equal. Thus, the minimum number of flips required is 4.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>
