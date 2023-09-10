<h2><a href="https://leetcode.com/problems/json-deep-equal/">2628. JSON Deep Equal</a></h2><h3>Medium</h3><hr><div><p>Given two objects <code>o1</code>&nbsp;and <code>o2</code>, check if they are <strong>deeply equal</strong>.</p>

<p>For two objects to be <strong>deeply equal</strong>, they must contain the same keys, and the associated values must also be&nbsp;<strong>deeply equal</strong>. Two objects are also considered&nbsp;<strong>deeply equal</strong>&nbsp;if they pass the&nbsp;<code>===</code>&nbsp;equality check.</p>

<p>You may assume both objects are the output of&nbsp;<code>JSON.parse</code>. In other words, they are valid JSON.</p>

<p>Please solve it without using lodash's&nbsp;<code>_.isEqual()</code>&nbsp;function.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> o1 = {"x":1,"y":2}, o2 = {"x":1,"y":2}
<strong>Output:</strong> true
<strong>Explanation:</strong> The keys and values match exactly.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> o1 = {"y":2,"x":1}, o2 = {"x":1,"y":2}
<strong>Output:</strong> true
<strong>Explanation:</strong> Although the keys are in a different order, they still match exactly.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> o1 = {"x":null,"L":[1,2,3]}, o2 = {"x":null,"L":["1","2","3"]}
<strong>Output:</strong> false
<strong>Explanation:</strong> The array of numbers is different from the array of strings.
</pre>

<p><strong class="example">Example 4:</strong></p>

<pre><strong>Input:</strong> o1 = true, o2 = false
<strong>Output:</strong> false
<strong>Explanation:</strong> true !== false</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= JSON.stringify(o1).length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= JSON.stringify(o2).length &lt;= 10<sup>5</sup></code></li>
	<li><code>maxNestingDepth &lt;= 1000</code></li>
</ul>
</div>