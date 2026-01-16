<h2><a href="https://leetcode.com/problems/maximize-area-of-square-hole-in-grid">3214. Maximize Area of Square Hole in Grid</a></h2><h3>Medium</h3><hr><p>You are given the two integers, <code>n</code> and <code>m</code> and two integer arrays, <code>hBars</code> and <code>vBars</code>. The grid has <code>n + 2</code> horizontal and <code>m + 2</code> vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from <code>1</code>.</p>

<p>You can <strong>remove</strong> some of the bars in <code>hBars</code> from horizontal bars and some of the bars in <code>vBars</code> from vertical bars. Note that other bars are fixed and cannot be removed.</p>

<p>Return an integer denoting the <strong>maximum area</strong> of a <em>square-shaped</em> hole in the grid, after removing some bars (possibly none).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/11/05/screenshot-from-2023-11-05-22-40-25.png" style="width: 411px; height: 220px;" /></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">n = 2, m = 1, hBars = [2,3], vBars = [2]</span></p>

<p><strong>Output: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The left image shows the initial grid formed by the bars. The horizontal bars are <code>[1,2,3,4]</code>, and the vertical bars are&nbsp;<code>[1,2,3]</code>.</p>

<p>One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/11/04/screenshot-from-2023-11-04-17-01-02.png" style="width: 368px; height: 145px;" /></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">n = 1, m = 1, hBars = [2], vBars = [2]</span></p>

<p><strong>Output: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">4</span></p>

<p><strong>Explanation:</strong></p>

<p>To get the maximum square-shaped hole, we remove horizontal bar 2 and vertical bar 2.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/03/12/unsaved-image-2.png" style="width: 648px; height: 218px;" /></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">n = 2, m = 3, hBars = [2,3], vBars = [2,4]</span></p>

<p><strong>Output: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">4</span></p>

<p><strong>Explanation:</strong></p>

<p><span style="color: var(--text-secondary); font-size: 0.875rem;">One way to get the maximum square-shaped hole is by removing horizontal bar 3, and vertical bar 4.</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= m &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= hBars.length &lt;= 100</code></li>
	<li><code>2 &lt;= hBars[i] &lt;= n + 1</code></li>
	<li><code>1 &lt;= vBars.length &lt;= 100</code></li>
	<li><code>2 &lt;= vBars[i] &lt;= m + 1</code></li>
	<li>All values in <code>hBars</code> are distinct.</li>
	<li>All values in <code>vBars</code> are distinct.</li>
</ul>
