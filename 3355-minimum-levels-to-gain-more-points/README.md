<h2><a href="https://leetcode.com/problems/minimum-levels-to-gain-more-points">3355. Minimum Levels to Gain More Points</a></h2><h3>Medium</h3><hr><p>You are given a binary array <code>possible</code> of length <code>n</code>.</p>

<p>Alice and Bob are playing a game that consists of <code>n</code> levels. Some of the levels in the game are <strong>impossible</strong> to clear while others can <strong>always</strong> be cleared. In particular, if <code>possible[i] == 0</code>, then the <code>i<sup>th</sup></code> level is <strong>impossible</strong> to clear for <strong>both</strong> the players. A player gains <code>1</code> point on clearing a level and loses <code>1</code> point if the player fails to clear it.</p>

<p>At the start of the game, Alice will play some levels in the <strong>given order</strong> starting from the <code>0<sup>th</sup></code> level, after which Bob will play for the rest of the levels.</p>

<p>Alice wants to know the <strong>minimum</strong> number of levels she should play to gain more points than Bob, if both players play optimally to <strong>maximize</strong> their points.</p>

<p>Return <em>the <strong>minimum</strong> number of levels Alice should play to gain more points</em>. <em>If this is <strong>not</strong> possible, return</em> <code>-1</code>.</p>

<p><strong>Note</strong> that each player must play at least <code>1</code> level.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">possible = [1,0,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Let&#39;s look at all the levels that Alice can play up to:</p>

<ul>
	<li>If Alice plays only level 0 and Bob plays the rest of the levels, Alice has 1 point, while Bob has -1 + 1 - 1 = -1 point.</li>
	<li>If Alice plays till level 1 and Bob plays the rest of the levels, Alice has 1 - 1 = 0 points, while Bob has 1 - 1 = 0 points.</li>
	<li>If Alice plays till level 2 and Bob plays the rest of the levels, Alice has 1 - 1 + 1 = 1 point, while Bob has -1 point.</li>
</ul>

<p>Alice must play a minimum of 1 level to gain more points.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">possible = [1,1,1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>Let&#39;s look at all the levels that Alice can play up to:</p>

<ul>
	<li>If Alice plays only level 0 and Bob plays the rest of the levels, Alice has 1 point, while Bob has 4 points.</li>
	<li>If Alice plays till level 1 and Bob plays the rest of the levels, Alice has 2 points, while Bob has 3 points.</li>
	<li>If Alice plays till level 2 and Bob plays the rest of the levels, Alice has 3 points, while Bob has 2 points.</li>
	<li>If Alice plays till level 3 and Bob plays the rest of the levels, Alice has 4 points, while Bob has 1 point.</li>
</ul>

<p>Alice must play a minimum of 3 levels to gain more points.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">possible = [0,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only possible way is for both players to play 1 level each. Alice plays level 0 and loses 1 point. Bob plays level 1 and loses 1 point. As both players have equal points, Alice can&#39;t gain more points than Bob.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n == possible.length &lt;= 10<sup>5</sup></code></li>
	<li><code>possible[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>
