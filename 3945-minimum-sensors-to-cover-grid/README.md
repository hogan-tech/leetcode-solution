<h2><a href="https://leetcode.com/problems/minimum-sensors-to-cover-grid">3945. Minimum Sensors to Cover Grid</a></h2><h3>Medium</h3><hr><p>You are given <code>n &times; m</code> grid and an integer <code>k</code>.</p>

<p>A sensor placed on cell <code>(r, c)</code> covers all cells whose <strong>Chebyshev distance</strong> from <code>(r, c)</code> is <strong>at most</strong> <code>k</code>.</p>

<p>The <strong>Chebyshev distance</strong> between two cells <code>(r<sub>1</sub>, c<sub>1</sub>)</code> and <code>(r<sub>2</sub>, c<sub>2</sub>)</code> is <code>max(|r<sub>1</sub> &minus; r<sub>2</sub>|,|c<sub>1</sub> &minus; c<sub>2</sub>|)</code>.</p>

<p>Your task is to return the <strong>minimum</strong> number of sensors required to cover every cell of the grid.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, m = 5, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>Placing sensors at positions <code>(0, 3)</code>, <code>(1, 0)</code>, <code>(3, 3)</code>, and <code>(4, 1)</code> ensures every cell in the grid is covered. Thus, the answer is 4.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2, m = 2, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>With <code>k = 2</code>, a single sensor can cover the entire <code>2 * 2</code> grid regardless of its position. Thus, the answer is 1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= m &lt;= 10<sup>3</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>3</sup></code></li>
</ul>
