<h2><a href="https://leetcode.com/problems/maximum-path-score-in-a-grid">3986. Maximum Path Score in a Grid</a></h2><h3>Medium</h3><hr><p>You are given an <code>m x n</code> grid where each cell contains one of the values 0, 1, or 2. You are also given an integer <code>k</code>.</p>

<p>You start from the top-left corner <code>(0, 0)</code> and want to reach the bottom-right corner <code>(m - 1, n - 1)</code> by moving only <strong>right</strong> or <strong>down</strong>.</p>

<p>Each cell contributes a specific score and incurs an associated cost, according to their cell values:</p>

<ul>
	<li>0: adds 0 to your score and costs 0.</li>
	<li>1: adds 1 to your score and costs 1.</li>
	<li>2: adds 2 to your score and costs 1. ​​​​​​​</li>
</ul>

<p>Return the <strong>maximum</strong> score achievable without exceeding a total cost of <code>k</code>, or -1 if no valid path exists.</p>

<p><strong>Note:</strong> If you reach the last cell but the total cost exceeds <code>k</code>, the path is invalid.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0, 1],[2, 0]], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<p>The optimal path is:</p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Cell</th>
			<th style="border: 1px solid black;">grid[i][j]</th>
			<th style="border: 1px solid black;">Score</th>
			<th style="border: 1px solid black;">Total<br />
			Score</th>
			<th style="border: 1px solid black;">Cost</th>
			<th style="border: 1px solid black;">Total<br />
			Cost</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">(0, 0)</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">(1, 0)</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">(1, 1)</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

<p>Thus, the maximum possible score is 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0, 1],[1, 2]], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no path that reaches cell <code>(1, 1)</code>​​​​​​​ without exceeding cost k. Thus, the answer is -1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>3</sup>​​​​​​​</code></li>
	<li><code><sup>​​​​​​​</sup>grid[0][0] == 0</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 2</code></li>
</ul>
