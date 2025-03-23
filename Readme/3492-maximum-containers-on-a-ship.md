<h2> 22 1
3492. Maximum Containers on a Ship</h2><hr><div><p>You are given a positive integer <code>n</code> representing an <code>n x n</code> cargo deck on a ship. Each cell on the deck can hold one container with a weight of <strong>exactly</strong> <code>w</code>.</p>

<p>However, the total weight of all containers, if loaded onto the deck, must not exceed the ship's maximum weight capacity, <code>maxWeight</code>.</p>

<p>Return the <strong>maximum</strong> number of containers that can be loaded onto the ship.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2, w = 3, maxWeight = 15</span></p>

<p><strong>Output:</strong> 4</p>

<p><strong>Explanation: </strong></p>

<p>The deck has 4 cells, and each container weighs 3. The total weight of loading all containers is 12, which does not exceed <code>maxWeight</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, w = 5, maxWeight = 20</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation: </strong></p>

<p>The deck has 9 cells, and each container weighs 5. The maximum number of containers that can be loaded without exceeding <code>maxWeight</code> is 4.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= w &lt;= 1000</code></li>
	<li><code>1 &lt;= maxWeight &lt;= 10<sup>9</sup></code></li>
</ul>
</div>