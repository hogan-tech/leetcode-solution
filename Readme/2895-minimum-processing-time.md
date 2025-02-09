<h2> 268 45
2895. Minimum Processing Time</h2><hr><div><p>You have a certain number of processors, each having 4 cores. The number of tasks to be executed is four times the number of processors. Each task must be assigned to a unique core, and each core can only be used once.</p>

<p>You are given an array <code>processorTime</code> representing the time each processor becomes available and an array <code>tasks</code> representing how long each task takes to complete. Return the&nbsp;<em>minimum</em> time needed to complete all tasks.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">processorTime = [8,10], tasks = [2,2,3,1,8,7,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">16</span></p>

<p><strong>Explanation:</strong></p>

<p>Assign the tasks at indices 4, 5, 6, 7 to the first processor which becomes available at <code>time = 8</code>, and the tasks at indices 0, 1, 2, 3 to the second processor which becomes available at <code>time = 10</code>.&nbsp;</p>

<p>The time taken by the first processor to finish the execution of all tasks is&nbsp;<code>max(8 + 8, 8 + 7, 8 + 4, 8 + 5) = 16</code>.</p>

<p>The time taken by the second processor to finish the execution of all tasks is&nbsp;<code>max(10 + 2, 10 + 2, 10 + 3, 10 + 1) = 13</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">processorTime = [10,20], tasks = [2,3,1,2,5,8,4,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">23</span></p>

<p><strong>Explanation:</strong></p>

<p>Assign the tasks at indices 1, 4, 5, 6 to the first processor and the others to the second processor.</p>

<p>The time taken by the first processor to finish the execution of all tasks is <code>max(10 + 3, 10 + 5, 10 + 8, 10 + 4) = 18</code>.</p>

<p>The time taken by the second processor to finish the execution of all tasks is <code>max(20 + 2, 20 + 1, 20 + 2, 20 + 3) = 23</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == processorTime.length &lt;= 25000</code></li>
	<li><code>1 &lt;= tasks.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= processorTime[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= tasks[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>tasks.length == 4 * n</code></li>
</ul>
</div>