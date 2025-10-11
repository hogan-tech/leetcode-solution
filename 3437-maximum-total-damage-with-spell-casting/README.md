<h2><a href="https://leetcode.com/problems/maximum-total-damage-with-spell-casting">3437. Maximum Total Damage With Spell Casting</a></h2><h3>Medium</h3><hr><p>A magician has various spells.</p>

<p>You are given an array <code>power</code>, where each element represents the damage of a spell. Multiple spells can have the same damage value.</p>

<p>It is a known fact that if a magician decides to cast a spell with a damage of <code>power[i]</code>, they <strong>cannot</strong> cast any spell with a damage of <code>power[i] - 2</code>, <code>power[i] - 1</code>, <code>power[i] + 1</code>, or <code>power[i] + 2</code>.</p>

<p>Each spell can be cast <strong>only once</strong>.</p>

<p>Return the <strong>maximum</strong> possible <em>total damage</em> that a magician can cast.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">power = [1,1,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">power = [7,1,6,6]</span></p>

<p><strong>Output:</strong> <span class="example-io">13</span></p>

<p><strong>Explanation:</strong></p>

<p>The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= power.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= power[i] &lt;= 10<sup>9</sup></code></li>
</ul>
