<h2> 40 13
3499. Maximize Active Section with Trade I</h2><hr><div><p>You are given a binary string <code>s</code> of length <code>n</code>, where:</p>

<ul>
	<li><code>'1'</code> represents an <strong>active</strong> section.</li>
	<li><code>'0'</code> represents an <strong>inactive</strong> section.</li>
</ul>

<p>You can perform <strong>at most one trade</strong> to maximize the number of active sections in <code>s</code>. In a trade, you:</p>

<ul>
	<li>Convert a contiguous block of <code>'1'</code>s that is surrounded by <code>'0'</code>s to all <code>'0'</code>s.</li>
	<li>Afterward, convert a contiguous block of <code>'0'</code>s that is surrounded by <code>'1'</code>s to all <code>'1'</code>s.</li>
</ul>

<p>Return the <strong>maximum</strong> number of active sections in <code>s</code> after making the optimal trade.</p>

<p><strong>Note:</strong> Treat <code>s</code> as if it is <strong>augmented</strong> with a <code>'1'</code> at both ends, forming <code>t = '1' + s + '1'</code>. The augmented <code>'1'</code>s <strong>do not</strong> contribute to the final count.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "01"</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Because there is no block of <code>'1'</code>s surrounded by <code>'0'</code>s, no valid trade is possible. The maximum number of active sections is 1.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "0100"</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>String <code>"0100"</code> → Augmented to <code>"101001"</code>.</li>
	<li>Choose <code>"0100"</code>, convert <code>"10<u><strong>1</strong></u>001"</code> → <code>"1<u><strong>0000</strong></u>1"</code> → <code>"1<u><strong>1111</strong></u>1"</code>.</li>
	<li>The final string without augmentation is <code>"1111"</code>. The maximum number of active sections is 4.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "1000100"</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>String <code>"1000100"</code> → Augmented to <code>"110001001"</code>.</li>
	<li>Choose <code>"000100"</code>, convert <code>"11000<u><strong>1</strong></u>001"</code> → <code>"11<u><strong>000000</strong></u>1"</code> → <code>"11<u><strong>111111</strong></u>1"</code>.</li>
	<li>The final string without augmentation is <code>"1111111"</code>. The maximum number of active sections is 7.</li>
</ul>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "01010"</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>String <code>"01010"</code> → Augmented to <code>"1010101"</code>.</li>
	<li>Choose <code>"010"</code>, convert <code>"10<u><strong>1</strong></u>0101"</code> → <code>"1<u><strong>000</strong></u>101"</code> → <code>"1<u><strong>111</strong></u>101"</code>.</li>
	<li>The final string without augmentation is <code>"11110"</code>. The maximum number of active sections is 4.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>'0'</code> or <code>'1'</code></li>
</ul>
</div>