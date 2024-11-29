<h2><a href="https://leetcode.com/problems/convert-object-to-json-string/">2633. Convert Object to JSON String</a></h2><h3>Medium</h3><hr><div><p>Given an object, return a valid JSON string of that object. You may assume the object only includes strings, integers, arrays, objects, booleans, and null. The returned string should not include extra spaces. The order of keys should be the same as the order returned by&nbsp;<code>Object.keys()</code>.</p>

<p>Please solve it without using the built-in <code>JSON.stringify</code> method.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> object = {"y":1,"x":2}
<strong>Output:</strong> {"y":1,"x":2}
<strong>Explanation:</strong> 
Return the JSON representation.
Note that the order of keys should be the same as the order returned by Object.keys().</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> object = {"a":"str","b":-12,"c":true,"d":null}
<strong>Output:</strong> {"a":"str","b":-12,"c":true,"d":null}
<strong>Explanation:</strong>
The primitives of JSON are strings, numbers, booleans, and null.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> object = {"key":{"a":1,"b":[{},null,"Hello"]}}
<strong>Output:</strong> {"key":{"a":1,"b":[{},null,"Hello"]}}
<strong>Explanation:</strong>
Objects and arrays can include other objects and arrays.
</pre>

<p><strong class="example">Example 4:</strong></p>

<pre><strong>Input:</strong> object = true
<strong>Output:</strong> true
<strong>Explanation:</strong>
Primitive types are valid inputs.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>object includes strings, integers, booleans, arrays, objects, and null</code></li>
	<li><code>1 &lt;= JSON.stringify(object).length &lt;= 10<sup>5</sup></code></li>
	<li><code>maxNestingLevel &lt;= 1000</code></li>
	<li><code>all strings will only contain alphanumeric characters</code></li>
</ul>
</div>