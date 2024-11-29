<h2><a href="https://leetcode.com/problems/array-of-objects-to-matrix/">2675. Array of Objects to Matrix</a></h2><h3>Medium</h3><hr><div><p>Write a function that converts an array of objects&nbsp;<code>arr</code> into a matrix <code>m</code>.</p>

<p><code>arr</code>&nbsp;is an array of objects or arrays. Each item in the array can be deeply nested with child arrays and child objects. It can also contain numbers, strings, booleans, and&nbsp;null values.</p>

<p>The first row <code>m</code>&nbsp;should be the column names. If there is no nesting, the column names are the unique keys within the objects. If there is nesting, the column names&nbsp;are the respective paths in the object separated by <code>"."</code>.</p>

<p>Each of the remaining rows corresponds to an object in&nbsp;<code>arr</code>. Each value in the matrix corresponds to a value in an object. If a given object doesn't contain a value for a given column, the cell should contain an empty string&nbsp;<code>""</code>.</p>

<p>The columns in the matrix should be in <strong>lexographically ascending</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> 
arr = [
&nbsp; {"b": 1, "a": 2},
&nbsp; {"b": 3, "a": 4}
]
<strong>Output:</strong> 
[
&nbsp; ["a", "b"],
&nbsp; [2, 1],
&nbsp; [4, 3]
]

<strong>Explanation:</strong>
There are two unique column names in the two objects: "a" and "b".
"a" corresponds with [2, 4].
"b" coresponds with [1, 3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> 
arr = [
&nbsp; {"a": 1, "b": 2},
&nbsp; {"c": 3, "d": 4},
&nbsp; {}
]
<strong>Output:</strong> 
[
&nbsp; ["a", "b", "c", "d"],
&nbsp; [1, 2, "", ""],
&nbsp; ["", "", 3, 4],
&nbsp; ["", "", "", ""]
]

<strong>Explanation:</strong>
There are 4 unique column names: "a", "b", "c", "d".
The first object has values associated with "a" and "b".
The second object has values associated with "c" and "d".
The third object has no keys, so it is just a row of empty strings.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> 
arr = [
&nbsp; {"a": {"b": 1, "c": 2}},
&nbsp; {"a": {"b": 3, "d": 4}}
]
<strong>Output:</strong> 
[
&nbsp; ["a.b", "a.c", "a.d"],
&nbsp; [1, 2, ""],
&nbsp; [3, "", 4]
]

<strong>Explanation:</strong>
In this example, the objects are nested. The keys represent the full path to each value separated by periods.
There are three paths: "a.b", "a.c", "a.d".
</pre>

<p><strong class="example">Example 4:</strong></p>

<pre><strong>Input:</strong> 
arr = [
&nbsp; [{"a": null}],
&nbsp; [{"b": true}],
&nbsp; [{"c": "x"}]
]
<strong>Output:</strong> 
[
&nbsp; ["0.a", "0.b", "0.c"],
&nbsp; [null, "", ""],
&nbsp; ["", true, ""],
&nbsp; ["", "", "x"]
]

<strong>Explanation:</strong>
Arrays are also considered objects with their keys being their indices.
Each array has one element so the keys are "0.a", "0.b", and "0.c".
</pre>

<p><strong class="example">Example 5:</strong></p>

<pre><strong>Input:</strong> 
arr = [
  {},
&nbsp; {},
&nbsp; {},
]
<strong>Output:</strong> 
[
&nbsp; [],
&nbsp; [],
&nbsp; [],
&nbsp; []
]

<strong>Explanation:</strong>
There are no keys so every row is an empty array.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>unique keys &lt;= 1000</code></li>
</ul>
</div>