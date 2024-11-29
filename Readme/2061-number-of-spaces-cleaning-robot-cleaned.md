<h2><a href="https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/">2061. Number of Spaces Cleaning Robot Cleaned</a></h2><h3>Medium</h3><hr><div><p>A room is represented by a <strong>0-indexed</strong> 2D binary matrix <code>room</code> where a <code>0</code> represents an <strong>empty</strong> space and a <code>1</code> represents a space with an <strong>object</strong>. The top left corner of the room will be empty in all test cases.</p>

<p>A cleaning robot starts at the top left corner of the room and is facing right. The robot will continue heading straight until it reaches the edge of the room or it hits an object, after which it will turn 90 degrees <strong>clockwise</strong> and repeat this process. The starting space and all spaces that the robot visits are <strong>cleaned</strong> by it.</p>

<p>Return <em>the number of <strong>clean</strong> spaces in the room if the robot runs indefinetely.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2021/11/01/image-20211101204703-1.png" style="width: 250px; height: 242px;">
<p>&nbsp;</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">room = [[0,0,0],[1,1,0],[0,0,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">7</span></p>

<p><strong>Explanation:</strong></p>

<ol>
	<li>​​​​​​​The robot cleans the spaces at (0, 0), (0, 1), and (0, 2).</li>
	<li>The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces down.</li>
	<li>The robot cleans the spaces at (1, 2), and (2, 2).</li>
	<li>The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces left.</li>
	<li>The robot cleans the spaces at (2, 1), and (2, 0).</li>
	<li>The robot has cleaned all 7 empty spaces, so return 7.</li>
</ol>
</div>

<p><strong class="example">Example 2:</strong></p>
<img src="https://assets.leetcode.com/uploads/2021/11/01/image-20211101204736-2.png" style="width: 250px; height: 245px;">
<p>&nbsp;</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">room = [[0,1,0],[1,0,0],[0,0,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ol>
	<li>The robot cleans the space at (0, 0).</li>
	<li>The robot hits an object, so it turns 90 degrees clockwise and now faces down.</li>
	<li>The robot hits an object, so it turns 90 degrees clockwise and now faces left.</li>
	<li>The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces up.</li>
	<li>The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces right.</li>
	<li>The robot is back at its starting position.</li>
	<li>The robot has cleaned 1 space, so return 1.</li>
</ol>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">room = [[0,0,0],[0,0,0],[0,0,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span>​​​​​​​</p>

<p>&nbsp;</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == room.length</code></li>
	<li><code>n == room[r].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>room[r][c]</code> is either <code>0</code> or <code>1</code>.</li>
	<li><code>room[0][0] == 0</code></li>
</ul>
</div>