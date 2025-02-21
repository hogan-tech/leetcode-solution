<h2> 1038 46
1529. Minimum Suffix Flips</h2><hr><div><p>You are given a <strong>0-indexed</strong> binary string <code>target</code> of length <code>n</code>. You have another binary string <code>s</code> of length <code>n</code> that is initially set to all zeros. You want to make <code>s</code> equal to <code>target</code>.</p>

<p>In one operation, you can pick an index <code>i</code> where <code>0 &lt;= i &lt; n</code> and flip all bits in the <strong>inclusive</strong> range <code>[i, n - 1]</code>. Flip means changing <code>'0'</code> to <code>'1'</code> and <code>'1'</code> to <code>'0'</code>.</p>

<p>Return <em>the minimum number of operations needed to make </em><code>s</code><em> equal to </em><code>target</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> target = "10111"
<strong>Output:</strong> 3
<strong>Explanation:</strong> Initially, s = "00000".
Choose index i = 2: "00<u>000</u>" -&gt; "00<u>111</u>"
Choose index i = 0: "<u>00111</u>" -&gt; "<u>11000</u>"
Choose index i = 1: "1<u>1000</u>" -&gt; "1<u>0111</u>"
We need at least 3 flip operations to form target.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> target = "101"
<strong>Output:</strong> 3
<strong>Explanation:</strong> Initially, s = "000".
Choose index i = 0: "<u>000</u>" -&gt; "<u>111</u>"
Choose index i = 1: "1<u>11</u>" -&gt; "1<u>00</u>"
Choose index i = 2: "10<u>0</u>" -&gt; "10<u>1</u>"
We need at least 3 flip operations to form target.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> target = "00000"
<strong>Output:</strong> 0
<strong>Explanation:</strong> We do not need any operations since the initial s already equals target.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == target.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>target[i]</code> is either <code>'0'</code> or <code>'1'</code>.</li>
</ul>
</div>