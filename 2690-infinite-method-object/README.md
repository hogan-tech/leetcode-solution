<h2><a href="https://leetcode.com/problems/infinite-method-object/">2690. Infinite Method Object</a></h2><h3>Easy</h3><hr><div><p>Write a function that&nbsp;returns an&nbsp;<strong>infinite-method</strong><strong>&nbsp;object</strong>.</p>

<p>An&nbsp;<strong>infinite-method</strong><strong>&nbsp;object</strong>&nbsp;is defined as an object that allows you to call any method and it will always return the name of the method.</p>

<p>For example, if you execute&nbsp;<code>obj.abc123()</code>, it will return&nbsp;<code>"abc123"</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> method = "abc123"
<strong>Output:</strong> "abc123"
<strong>Explanation:</strong>
const obj = createInfiniteObject();
obj['abc123'](); // "abc123"
The returned string should always match the method name.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> method = ".-qw73n|^2It"
<strong>Output:</strong> ".-qw73n|^2It"
<strong>Explanation:</strong> The returned string should always match the method name.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= method.length &lt;= 1000</code></li>
</ul>
</div>