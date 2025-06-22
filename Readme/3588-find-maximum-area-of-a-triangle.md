<h2><a href="https://leetcode.com/problems/find-maximum-area-of-a-triangle">3868. Find Maximum Area of a Triangle</a></h2><h3>Medium</h3><hr><p>You are given a 2D array <code>coords</code> of size <code>n x 2</code>, representing the coordinates of <code>n</code> points in an infinite Cartesian plane.</p>

<p>Find <strong>twice</strong> the <strong>maximum</strong> area of a triangle with its corners at <em>any</em> three elements from <code>coords</code>, such that at least one side of this triangle is <strong>parallel</strong> to the x-axis or y-axis. Formally, if the maximum area of such a triangle is <code>A</code>, return <code>2 * A</code>.</p>

<p>If no such triangle exists, return -1.</p>

<p><strong>Note</strong> that a triangle <em>cannot</em> have zero area.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">coords = [[1,1],[1,2],[3,2],[3,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2025/04/19/image-20250420010047-1.png" style="width: 300px; height: 289px;" /></p>

<p>The triangle shown in the image has a base 1 and height 2. Hence its area is <code>1/2 * base * height = 1</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">coords = [[1,1],[2,2],[3,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only possible triangle has corners <code>(1, 1)</code>, <code>(2, 2)</code>, and <code>(3, 3)</code>. None of its sides are parallel to the x-axis or the y-axis.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == coords.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= coords[i][0], coords[i][1] &lt;= 10<sup>6</sup></code></li>
	<li>All <code>coords[i]</code> are <strong>unique</strong>.</li>
</ul>
