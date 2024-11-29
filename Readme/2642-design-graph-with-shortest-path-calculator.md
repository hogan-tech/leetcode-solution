<h2><a href="https://leetcode.com/problems/design-graph-with-shortest-path-calculator/">2642. Design Graph With Shortest Path Calculator</a></h2><h3>Hard</h3><hr><div><p>There is a <strong>directed weighted</strong> graph that consists of <code>n</code> nodes numbered from <code>0</code> to <code>n - 1</code>. The edges of the graph are initially represented by the given array <code>edges</code> where <code>edges[i] = [from<sub>i</sub>, to<sub>i</sub>, edgeCost<sub>i</sub>]</code> meaning that there is an edge from <code>from<sub>i</sub></code> to <code>to<sub>i</sub></code> with the cost <code>edgeCost<sub>i</sub></code>.</p>

<p>Implement the <code>Graph</code> class:</p>

<ul>
	<li><code>Graph(int n, int[][] edges)</code> initializes the object with <code>n</code> nodes and the given edges.</li>
	<li><code>addEdge(int[] edge)</code> adds an edge to the list of edges where <code>edge = [from, to, edgeCost]</code>. It is guaranteed that there is no edge between the two nodes before adding this one.</li>
	<li><code>int shortestPath(int node1, int node2)</code> returns the <strong>minimum</strong> cost of a path from <code>node1</code> to <code>node2</code>. If no path exists, return <code>-1</code>. The cost of a path is the sum of the costs of the edges in the path.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/01/11/graph3drawio-2.png" style="width: 621px; height: 191px;">
<pre><strong>Input</strong>
["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
<strong>Output</strong>
[null, 6, -1, null, 6]

<strong>Explanation</strong>
Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 in the first diagram above is 3 -&gt; 0 -&gt; 1 -&gt; 2 with a total cost of 3 + 2 + 1 = 6.
g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the second diagram above.
g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 now is 0 -&gt; 1 -&gt; 3 with a total cost of 2 + 4 = 6.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>0 &lt;= edges.length &lt;= n * (n - 1)</code></li>
	<li><code>edges[i].length == edge.length == 3</code></li>
	<li><code>0 &lt;= from<sub>i</sub>, to<sub>i</sub>, from, to, node1, node2 &lt;= n - 1</code></li>
	<li><code>1 &lt;= edgeCost<sub>i</sub>, edgeCost &lt;= 10<sup>6</sup></code></li>
	<li>There are no repeated edges and no self-loops in the graph at any point.</li>
	<li>At most <code>100</code> calls will be made for <code>addEdge</code>.</li>
	<li>At most <code>100</code> calls will be made for <code>shortestPath</code>.</li>
</ul>
</div>