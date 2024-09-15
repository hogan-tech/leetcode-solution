<h2><a href="https://leetcode.com/problems/maximum-multiplication-score/">3290. Maximum Multiplication Score</a></h2><h3>Medium</h3><hr><div><p>You are given an integer array <code>a</code> of size 4 and another integer array <code>b</code> of size <strong>at least</strong> 4.</p>

<p>You need to choose 4 indices <code>i<sub>0</sub></code>, <code>i<sub>1</sub></code>, <code>i<sub>2</sub></code>, and <code>i<sub>3</sub></code> from the array <code>b</code> such that <code>i<sub>0</sub> &lt; i<sub>1</sub> &lt; i<sub>2</sub> &lt; i<sub>3</sub></code>. Your score will be equal to the value <code>a[0] * b[i<sub>0</sub>] + a[1] * b[i<sub>1</sub>] + a[2] * b[i<sub>2</sub>] + a[3] * b[i<sub>3</sub>]</code>.</p>

<p>Return the <strong>maximum</strong> score you can achieve.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">a = [3,2,5,6], b = [2,-6,4,-5,-3,2,-7]</span></p>

<p><strong>Output:</strong> <span class="example-io">26</span></p>

<p><strong>Explanation:</strong><br>
We can choose the indices 0, 1, 2, and 5. The score will be <code>3 * 2 + 2 * (-6) + 5 * 4 + 6 * 2 = 26</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">a = [-1,4,5,-2], b = [-5,-1,-3,-2,-4]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong><br>
We can choose the indices 0, 1, 3, and 4. The score will be <code>(-1) * (-5) + 4 * (-1) + 5 * (-2) + (-2) * (-4) = -1</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>a.length == 4</code></li>
	<li><code>4 &lt;= b.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= a[i], b[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</div>