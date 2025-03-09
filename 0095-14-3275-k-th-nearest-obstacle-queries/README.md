<h2> 95 14
3275. K-th Nearest Obstacle Queries</h2><hr><div><p>There is an infinite 2D plane.</p>

<p>You are given a positive integer <code>k</code>. You are also given a 2D array <code>queries</code>, which contains the following queries:</p>

<ul>
	<li><code>queries[i] = [x, y]</code>: Build an obstacle at coordinate <code>(x, y)</code> in the plane. It is guaranteed that there is <strong>no</strong> obstacle at this coordinate when this query is made.</li>
</ul>

<p>After each query, you need to find the <strong>distance</strong> of the <code>k<sup>th</sup></code> <strong>nearest</strong> obstacle from the origin.</p>

<p>Return an integer array <code>results</code> where <code>results[i]</code> denotes the <code>k<sup>th</sup></code> nearest obstacle after query <code>i</code>, or <code>results[i] == -1</code> if there are less than <code>k</code> obstacles.</p>

<p><strong>Note</strong> that initially there are <strong>no</strong> obstacles anywhere.</p>

<p>The <strong>distance</strong> of an obstacle at coordinate <code>(x, y)</code> from the origin is given by <code>|x| + |y|</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">queries = [[1,2],[3,4],[2,3],[-3,0]], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,7,5,3]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Initially, there are 0 obstacles.</li>
	<li>After <code>queries[0]</code>, there are less than 2 obstacles.</li>
	<li>After <code>queries[1]</code>, there are obstacles at distances 3 and 7.</li>
	<li>After <code>queries[2]</code>, there are obstacles at distances 3, 5, and 7.</li>
	<li>After <code>queries[3]</code>, there are obstacles at distances 3, 3, 5, and 7.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">queries = [[5,5],[4,4],[3,3]], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">[10,8,6]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>After <code>queries[0]</code>, there is an obstacle at distance 10.</li>
	<li>After <code>queries[1]</code>, there are obstacles at distances 8 and 10.</li>
	<li>After <code>queries[2]</code>, there are obstacles at distances 6, 8, and 10.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= queries.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li>All <code>queries[i]</code> are unique.</li>
	<li><code>-10<sup>9</sup> &lt;= queries[i][0], queries[i][1] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>
</div>