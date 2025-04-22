<h2><a href="https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels">302. Smallest Rectangle Enclosing Black Pixels</a></h2><h3>Hard</h3><hr><p>You are given an <code>m x n</code> binary matrix <code>image</code> where <code>0</code> represents a white pixel and <code>1</code> represents a black pixel.</p>

<p>The black pixels are connected (i.e., there is only one black region). Pixels are connected horizontally and vertically.</p>

<p>Given two integers <code>x</code> and <code>y</code> that represents the location of one of the black pixels, return <em>the area of the smallest (axis-aligned) rectangle that encloses all black pixels</em>.</p>

<p>You must write an algorithm with less than <code>O(mn)</code> runtime complexity</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/pixel-grid.jpg" style="width: 333px; height: 253px;" />
<pre>
<strong>Input:</strong> image = [[&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;],[&quot;0&quot;,&quot;1&quot;,&quot;1&quot;,&quot;0&quot;],[&quot;0&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;]], x = 0, y = 2
<strong>Output:</strong> 6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> image = [[&quot;1&quot;]], x = 0, y = 0
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == image.length</code></li>
	<li><code>n == image[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>image[i][j]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
	<li><code>0 &lt;= x &lt; m</code></li>
	<li><code>0 &lt;= y &lt; n</code></li>
	<li><code>image[x][y] == &#39;1&#39;.</code></li>
	<li>The black pixels in the <code>image</code> only form <strong>one component</strong>.</li>
</ul>
