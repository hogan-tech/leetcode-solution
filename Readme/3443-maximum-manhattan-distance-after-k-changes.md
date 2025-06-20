<h2><a href="https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes">3754. Maximum Manhattan Distance After K Changes</a></h2><h3>Medium</h3><hr><p>You are given a string <code>s</code> consisting of the characters <code>&#39;N&#39;</code>, <code>&#39;S&#39;</code>, <code>&#39;E&#39;</code>, and <code>&#39;W&#39;</code>, where <code>s[i]</code> indicates movements in an infinite grid:</p>

<ul>
	<li><code>&#39;N&#39;</code> : Move north by 1 unit.</li>
	<li><code>&#39;S&#39;</code> : Move south by 1 unit.</li>
	<li><code>&#39;E&#39;</code> : Move east by 1 unit.</li>
	<li><code>&#39;W&#39;</code> : Move west by 1 unit.</li>
</ul>

<p>Initially, you are at the origin <code>(0, 0)</code>. You can change <strong>at most</strong> <code>k</code> characters to any of the four directions.</p>

<p>Find the <strong>maximum</strong> <strong>Manhattan distance</strong> from the origin that can be achieved <strong>at any time</strong> while performing the movements <strong>in order</strong>.</p>
The <strong>Manhattan Distance</strong> between two cells <code>(x<sub>i</sub>, y<sub>i</sub>)</code> and <code>(x<sub>j</sub>, y<sub>j</sub>)</code> is <code>|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;NWSE&quot;, k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>Change <code>s[2]</code> from <code>&#39;S&#39;</code> to <code>&#39;N&#39;</code>. The string <code>s</code> becomes <code>&quot;NWNE&quot;</code>.</p>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Movement</th>
			<th style="border: 1px solid black;">Position (x, y)</th>
			<th style="border: 1px solid black;">Manhattan Distance</th>
			<th style="border: 1px solid black;">Maximum</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">s[0] == &#39;N&#39;</td>
			<td style="border: 1px solid black;">(0, 1)</td>
			<td style="border: 1px solid black;">0 + 1 = 1</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">s[1] == &#39;W&#39;</td>
			<td style="border: 1px solid black;">(-1, 1)</td>
			<td style="border: 1px solid black;">1 + 1 = 2</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">s[2] == &#39;N&#39;</td>
			<td style="border: 1px solid black;">(-1, 2)</td>
			<td style="border: 1px solid black;">1 + 2 = 3</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">s[3] == &#39;E&#39;</td>
			<td style="border: 1px solid black;">(0, 2)</td>
			<td style="border: 1px solid black;">0 + 2 = 2</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
	</tbody>
</table>

<p>The maximum Manhattan distance from the origin that can be achieved is 3. Hence, 3 is the output.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;NSWWEW&quot;, k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>Change <code>s[1]</code> from <code>&#39;S&#39;</code> to <code>&#39;N&#39;</code>, and <code>s[4]</code> from <code>&#39;E&#39;</code> to <code>&#39;W&#39;</code>. The string <code>s</code> becomes <code>&quot;NNWWWW&quot;</code>.</p>

<p>The maximum Manhattan distance from the origin that can be achieved is 6. Hence, 6 is the output.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= s.length</code></li>
	<li><code>s</code> consists of only <code>&#39;N&#39;</code>, <code>&#39;S&#39;</code>, <code>&#39;E&#39;</code>, and <code>&#39;W&#39;</code>.</li>
</ul>
