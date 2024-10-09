<h2><a href="https://leetcode.com/problems/maximum-coins-heroes-can-collect/solution/">2838. Maximum Coins Heroes Can Collect</a></h2><h3>Medium</h3><hr><div><p>There is a battle and <code>n</code> heroes are trying to defeat <code>m</code> monsters. You are given two <strong>1-indexed</strong> arrays of <strong>positive</strong> integers <code><font face="monospace">heroes</font></code> and <code><font face="monospace">monsters</font></code> of length <code>n</code> and <code>m</code>, respectively. <code><font face="monospace">heroes</font>[i]</code> is the power of <code>i<sup>th</sup></code> hero, and <code><font face="monospace">monsters</font>[i]</code> is the power of <code>i<sup>th</sup></code> monster.</p>

<p>The <code>i<sup>th</sup></code> hero can defeat the <code>j<sup>th</sup></code> monster if <code>monsters[j] &lt;= heroes[i]</code>.</p>

<p>You are also given a <strong>1-indexed</strong> array <code>coins</code> of length <code>m</code> consisting of <strong>positive</strong> integers. <code>coins[i]</code> is the number of coins that each hero earns after defeating the <code>i<sup>th</sup></code> monster.</p>

<p>Return<em> an array </em><code>ans</code><em> of length </em><code>n</code><em> where </em><code>ans[i]</code><em> is the <strong>maximum</strong> number of coins that the </em><code>i<sup>th</sup></code><em> hero can collect from this battle</em>.</p>

<p><strong>Notes</strong></p>

<ul>
	<li>The health of a hero doesn't get reduced after defeating a monster.</li>
	<li>Multiple heroes can defeat a monster, but each monster can be defeated by a given hero only once.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> heroes = [1,4,2], monsters = [1,1,5,2,3], coins = [2,3,4,5,6]
<strong>Output:</strong> [5,16,10]
<strong>Explanation: </strong>For each hero, we list the index of all the monsters he can defeat:
1<sup>st</sup> hero: [1,2] since the power of this hero is 1 and monsters[1], monsters[2] &lt;= 1. So this hero collects coins[1] + coins[2] = 5 coins.
2<sup>nd</sup> hero: [1,2,4,5] since the power of this hero is 4 and monsters[1], monsters[2], monsters[4], monsters[5] &lt;= 4. So this hero collects coins[1] + coins[2] + coins[4] + coins[5] = 16 coins.
3<sup>rd</sup> hero: [1,2,4] since the power of this hero is 2 and monsters[1], monsters[2], monsters[4] &lt;= 2. So this hero collects coins[1] + coins[2] + coins[4] = 10 coins.
So the answer would be [5,16,10].</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> heroes = [5], monsters = [2,3,1,2], coins = [10,6,5,2]
<strong>Output:</strong> [23]
<strong>Explanation:</strong> This hero can defeat all the monsters since monsters[i] &lt;= 5. So he collects all of the coins: coins[1] + coins[2] + coins[3] + coins[4] = 23, and the answer would be [23].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> heroes = [4,4], monsters = [5,7,8], coins = [1,1,1]
<strong>Output:</strong> [0,0]
<strong>Explanation:</strong> In this example, no hero can defeat a monster. So the answer would be [0,0],
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == heroes.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m == monsters.length &lt;= 10<sup>5</sup></code></li>
	<li><code>coins.length == m</code></li>
	<li><code>1 &lt;= heroes[i], monsters[i], coins[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>