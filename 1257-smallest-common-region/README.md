<h2><a href="https://leetcode.com/problems/smallest-common-region/">1257. Smallest Common Region</a></h2><h3>Medium</h3><hr><div><p>You are given some lists of <code>regions</code> where the first region of each list includes all other regions in that list.</p>

<p>Naturally, if a region <code>x</code> contains another region <code>y</code> then <code>x</code> is bigger than <code>y</code>. Also, by definition, a region <code>x</code> contains itself.</p>

<p>Given two regions: <code>region1</code> and <code>region2</code>, return <em>the smallest region that contains both of them</em>.</p>

<p>If you are given regions <code>r1</code>, <code>r2</code>, and <code>r3</code> such that <code>r1</code> includes <code>r3</code>, it is guaranteed there is no <code>r2</code> such that <code>r2</code> includes <code>r3</code>.</p>

<p>It is guaranteed the smallest region exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:
</strong>regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
<strong>Output:</strong> "North America"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> regions = [["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]], region1 = "Canada", region2 = "South America"
<strong>Output:</strong> "Earth"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= regions.length &lt;= 10<sup>4</sup></code></li>
	<li><code>2 &lt;= regions[i].length &lt;= 20</code></li>
	<li><code>1 &lt;= regions[i][j].length, region1.length, region2.length &lt;= 20</code></li>
	<li><code>region1 != region2</code></li>
	<li><code>regions[i][j]</code>, <code>region1</code>, and <code>region2</code> consist of English letters.</li>
</ul>
</div>