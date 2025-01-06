<h2> 22 0
2814. Minimum Time Takes to Reach Destination Without Drowning</h2><hr><div><p>You are given an <code>n * m</code> <strong>0-indexed</strong> grid of string <code>land</code>. Right now, you are standing at the cell that contains <code>"S"</code>, and you want to get to the cell containing <code>"D"</code>. There are three other types of cells in this land:</p>

<ul>
	<li><code>"."</code>: These cells are empty.</li>
	<li><code>"X"</code>: These cells are stone.</li>
	<li><code>"*"</code>: These cells are flooded.</li>
</ul>

<p>At each second, you can move to a cell that shares a side with your current cell (if it exists). Also, at each second, every <strong>empty cell</strong> that shares a side with a flooded cell becomes flooded as well.<br>
There are two problems ahead of your journey:</p>

<ul>
	<li>You can't step on stone cells.</li>
	<li>You can't step on flooded cells since you will drown (also, you can't step on a cell that will be flooded at the same time as you step on it).</li>
</ul>

<p>Return<em> the <strong>minimum</strong> time it takes you to reach the destination in seconds, or </em><code>-1</code><em> if it is impossible.</em></p>

<p><strong>Note</strong> that the destination will never be flooded.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> land = [["D",".","*"],[".",".","."],[".","S","."]]
<strong>Output:</strong> 3
<strong>Explanation: </strong>The picture below shows the simulation of the land second by second. The blue cells are flooded, and the gray cells are stone.
Picture (0) shows the initial state and picture (3) shows the final state when we reach destination. As you see, it takes us 3 second to reach destination and the answer would be 3.
It can be shown that 3 is the minimum time needed to reach from S to D.
</pre>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/08/09/ex1.png" style="padding: 5px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 600px; height: 111px;"></p>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> land = [["D","X","*"],[".",".","."],[".",".","S"]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> The picture below shows the simulation of the land second by second. The blue cells are flooded, and the gray cells are stone.
Picture (0) shows the initial state. As you see, no matter which paths we choose, we will drown at the 3<sup>rd</sup>&nbsp;second. Also the minimum path takes us 4 seconds to reach from S to D.
So the answer would be -1.
</pre>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/08/09/ex2-2.png" style="padding: 7px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 600px; height: 107px;"></p>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> land = [["D",".",".",".","*","."],[".","X",".","X",".","."],[".",".",".",".","S","."]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> It can be shown that we can reach destination in 6 seconds. Also it can be shown that 6 is the minimum seconds one need to reach from S to D.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n, m &lt;= 100</code></li>
	<li><code>land</code>&nbsp;consists only of&nbsp;<code>"S"</code>, <code>"D"</code>, <code>"."</code>, <code>"*"</code> and&nbsp;<code>"X"</code>.</li>
	<li><strong>Exactly</strong> one of the cells is equal to <code>"S"</code>.</li>
	<li><strong>Exactly</strong> one of the cells is equal to <code>"D"</code>.</li>
</ul>
</div>