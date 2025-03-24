<h2> 248 6
3169. Count Days Without Meetings</h2><hr><div><p>You are given a positive integer <code>days</code> representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array <code>meetings</code> of size <code>n</code> where, <code>meetings[i] = [start_i, end_i]</code> represents the starting and ending days of meeting <code>i</code> (inclusive).</p>

<p>Return the count of days when the employee is available for work but no meetings are scheduled.</p>

<p><strong>Note: </strong>The meetings may overlap.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">days = 10, meetings = [[5,7],[1,3],[9,10]]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no meeting scheduled on the 4<sup>th</sup> and 8<sup>th</sup> days.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">days = 5, meetings = [[2,4],[1,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no meeting scheduled on the 5<sup>th </sup>day.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">days = 6, meetings = [[1,6]]</span></p>

<p><strong>Output:</strong> 0</p>

<p><strong>Explanation:</strong></p>

<p>Meetings are scheduled for all working days.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= days &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= meetings.length &lt;= 10<sup>5</sup></code></li>
	<li><code>meetings[i].length == 2</code></li>
	<li><code><font face="monospace">1 &lt;= meetings[i][0] &lt;= meetings[i][1] &lt;= days</font></code></li>
</ul>
</div>