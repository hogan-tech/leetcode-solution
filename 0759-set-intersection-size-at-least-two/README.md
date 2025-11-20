<h2><a href="https://leetcode.com/problems/set-intersection-size-at-least-two">759. Set Intersection Size At Least Two</a></h2><h3>Hard</h3><hr><p>You are given a 2D integer array <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> represents all the integers from <code>start<sub>i</sub></code> to <code>end<sub>i</sub></code> inclusively.</p>

<p>A <strong>containing set</strong> is an array <code>nums</code> where each interval from <code>intervals</code> has <strong>at least two</strong> integers in <code>nums</code>.</p>

<ul>
	<li>For example, if <code>intervals = [[1,3], [3,7], [8,9]]</code>, then <code>[1,2,4,7,8,9]</code> and <code>[2,3,4,8,9]</code> are <strong>containing sets</strong>.</li>
</ul>

<p>Return <em>the minimum possible size of a containing set</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,3],[3,7],[8,9]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> let nums = [2, 3, 4, 8, 9].
It can be shown that there cannot be any containing array of size 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,3],[1,4],[2,5],[3,5]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> let nums = [2, 3, 4].
It can be shown that there cannot be any containing array of size 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> intervals = [[1,2],[2,3],[2,4],[4,5]]
<strong>Output:</strong> 5
<strong>Explanation:</strong> let nums = [1, 2, 3, 4, 5].
It can be shown that there cannot be any containing array of size 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 3000</code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 10<sup>8</sup></code></li>
</ul>
