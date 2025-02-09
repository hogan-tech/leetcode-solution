<h2> 2 1
3447. Assign Elements to Groups with Constraints</h2><hr><div><p>You are given an integer array <code>groups</code>, where <code>groups[i]</code> represents the size of the <code>i<sup>th</sup></code> group. You are also given an integer array <code>elements</code>.</p>

<p>Your task is to assign <strong>one</strong> element to each group based on the following rules:</p>

<ul>
	<li>An element <code>j</code> can be assigned to a group <code>i</code> if <code>groups[i]</code> is <strong>divisible</strong> by <code>elements[j]</code>.</li>
	<li>If there are multiple elements that can be assigned, assign the element with the <strong>smallest index</strong> <code>j</code>.</li>
	<li>If no element satisfies the condition for a group, assign -1 to that group.</li>
</ul>

<p>Return an integer array <code>assigned</code>, where <code>assigned[i]</code> is the index of the element chosen for group <code>i</code>, or -1 if no suitable element exists.</p>

<p><strong>Note</strong>: An element may be assigned to more than one group.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">groups = [8,4,3,2,4], elements = [4,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,0,-1,1,0]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>elements[0] = 4</code> is assigned to groups 0, 1, and 4.</li>
	<li><code>elements[1] = 2</code> is assigned to group 3.</li>
	<li>Group 2 cannot be assigned any element.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">groups = [2,3,5,7], elements = [5,3,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,1,0,-1]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li><code>elements[1] = 3</code> is assigned to group 1.</li>
	<li><code>elements[0] = 5</code> is assigned to group 2.</li>
	<li>Groups 0 and 3 cannot be assigned any element.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">groups = [10,21,30,41], elements = [2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1,0,1]</span></p>

<p><strong>Explanation:</strong></p>

<p><code>elements[0] = 2</code> is assigned to the groups with even values, and <code>elements[1] = 1</code> is assigned to the groups with odd values.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= groups.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= elements.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= groups[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= elements[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</div>