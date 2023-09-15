<h2><a href="https://leetcode.com/problems/make-object-immutable/">2692. Make Object Immutable</a></h2><h3>Medium</h3><hr><div><p>Write a function that takes an object&nbsp;<code>obj</code> and returns a new&nbsp;<strong>immutable</strong>&nbsp;version of this object.</p>

<p>An&nbsp;<strong>immutable&nbsp;</strong>object is an object that can't be altered and will throw an error if any attempt is made to alter it.</p>

<p>There are three types of error messages that can be produced from this new object.</p>

<ul>
	<li>Attempting to modify a key on the object will result in this&nbsp;error message: <code>`Error Modifying: ${key}`</code>.</li>
	<li>Attempting to modify an index on an array will result in this error message: <code>`Error Modifying&nbsp;Index: ${index}`</code>.</li>
	<li>Attempting to call a method that mutates an array will result in this error message: <code>`Error Calling Method: ${methodName}`</code>. You may assume the only methods that can mutate&nbsp;an array are&nbsp;<code>['pop', 'push', 'shift', 'unshift', 'splice', 'sort', 'reverse']</code>.</li>
</ul>

<p><code>obj</code>&nbsp;is a valid JSON object or array, meaning it is the output of <code>JSON.parse()</code>.</p>

<p>Note that a string literal should be thrown, not an&nbsp;<code>Error</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> 
obj = {
&nbsp; "x": 5
}
fn = (obj) =&gt; { 
&nbsp; obj.x = 5;
&nbsp; return obj.x;
}
<strong>Output:</strong> {"value": null, "error": "Error Modifying:&nbsp;x"}
<strong>Explanation: </strong>Attempting to modify a key on an object resuts in a thrown error. Note that it doesn't matter that the value was set to the same value as it was before.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> 
obj = [1, 2, 3]
fn = (arr) =&gt; { 
&nbsp; arr[1] = {}; 
&nbsp; return arr[2]; 
}
<strong>Output:</strong> {"value": null, "error": "Error Modifying&nbsp;Index: 1"}
<strong>Explanation: </strong>Attempting to modify an array results in a thrown error.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> 
obj = {
&nbsp; "arr": [1, 2, 3]
}
fn = (obj) =&gt; { 
&nbsp; obj.arr.push(4);
&nbsp; return 42;
}
<strong>Output:</strong> { "value": null, "error": "Error Calling Method: push"}
<strong>Explanation: </strong>Calling a method that can result in a mutation results in a thrown error.
</pre>

<p><strong class="example">Example 4:</strong></p>

<pre><strong>Input:</strong> 
obj = {
&nbsp; "x": 2,
&nbsp; "y": 2
}
fn = (obj) =&gt; { 
&nbsp; return Object.keys(obj);
}
<strong>Output:</strong> {"value": ["x", "y"], "error": null}
<strong>Explanation: </strong>No mutations were attempted so the function returns as normal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= JSON.stringify(obj).length &lt;= 10<sup>5</sup></code></li>
</ul>
</div>