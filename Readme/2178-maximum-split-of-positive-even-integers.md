<h2><a href="https://leetcode.com/problems/maximum-split-of-positive-even-integers">2279. Maximum Split of Positive Even Integers</a></h2><h3>Medium</h3><hr><p>You are given an integer <code>finalSum</code>. Split it into a sum of a <strong>maximum</strong> number of <strong>unique</strong> positive even integers.</p>

<ul>
	<li>For example, given <code>finalSum = 12</code>, the following splits are <strong>valid</strong> (unique positive even integers summing up to <code>finalSum</code>): <code>(12)</code>, <code>(2 + 10)</code>, <code>(2 + 4 + 6)</code>, and <code>(4 + 8)</code>. Among them, <code>(2 + 4 + 6)</code> contains the maximum number of integers. Note that <code>finalSum</code> cannot be split into <code>(2 + 2 + 4 + 4)</code> as all the numbers should be unique.</li>
</ul>

<p>Return <em>a list of integers that represent a valid split containing a <strong>maximum</strong> number of integers</em>. If no valid split exists for <code>finalSum</code>, return <em>an <strong>empty</strong> list</em>. You may return the integers in <strong>any</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> finalSum = 12
<strong>Output:</strong> [2,4,6]
<strong>Explanation:</strong> The following are valid splits: <code>(12)</code>, <code>(2 + 10)</code>, <code>(2 + 4 + 6)</code>, and <code>(4 + 8)</code>.
(2 + 4 + 6) has the maximum number of integers, which is 3. Thus, we return [2,4,6].
Note that [2,6,4], [6,2,4], etc. are also accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> finalSum = 7
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no valid splits for the given finalSum.
Thus, we return an empty array.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> finalSum = 28
<strong>Output:</strong> [6,8,2,12]
<strong>Explanation:</strong> The following are valid splits: <code>(2 + 26)</code>, <code>(6 + 8 + 2 + 12)</code>, and <code>(4 + 24)</code>. 
<code>(6 + 8 + 2 + 12)</code> has the maximum number of integers, which is 4. Thus, we return [6,8,2,12].
Note that [10,2,4,12], [6,2,4,16], etc. are also accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= finalSum &lt;= 10<sup>10</sup></code></li>
</ul>
