<h2><a href="https://leetcode.com/problems/memoize-ii/">2630. Memoize II</a></h2><h3>Hard</h3><hr><div><p>Given a function <code>fn</code>,&nbsp;return&nbsp;a&nbsp;<strong>memoized</strong>&nbsp;version of that function.</p>

<p>A&nbsp;<strong>memoized&nbsp;</strong>function is a function that will never be called twice with&nbsp;the same inputs. Instead it will return&nbsp;a cached value.</p>

<p><code>fn</code>&nbsp;can be any function and there are no constraints on what type of values it accepts. Inputs are considered identical if they are&nbsp;<code>===</code> to each other.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> 
getInputs = () =&gt; [[2,2],[2,2],[1,2]]
fn = function (a, b) { return a + b; }
<strong>Output:</strong> [{"val":4,"calls":1},{"val":4,"calls":1},{"val":3,"calls":2}]
<strong>Explanation:</strong>
const inputs = getInputs();
const memoized = memoize(fn);
for (const arr of inputs) {
  memoized(...arr);
}

For the inputs of (2, 2): 2 + 2 = 4, and it required a call to fn().
For the inputs of (2, 2): 2 + 2 = 4, but those inputs were seen before so no call to fn() was required.
For the inputs of (1, 2): 1 + 2 = 3, and it required another call to fn() for a total of 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> 
getInputs = () =&gt; [[{},{}],[{},{}],[{},{}]] 
fn = function (a, b) { return ({...a, ...b}); }
<strong>Output:</strong> [{"val":{},"calls":1},{"val":{},"calls":2},{"val":{},"calls":3}]
<strong>Explanation:</strong>
Merging two empty objects will always result in an empty object. It may seem like there should only be 1&nbsp;call to fn() because of cache-hits, however none of those objects are === to each other.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> 
getInputs = () =&gt; { const o = {}; return [[o,o],[o,o],[o,o]]; }
fn = function (a, b) { return ({...a, ...b}); }
<strong>Output:</strong> [{"val":{},"calls":1},{"val":{},"calls":1},{"val":{},"calls":1}]
<strong>Explanation:</strong>
Merging two empty objects will always result in an empty object. The 2nd and 3rd third function calls result in a cache-hit. This is because every object passed in is identical.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= inputs.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= inputs.flat().length &lt;= 10<sup>5</sup></code></li>
	<li><code>inputs[i][j] != NaN</code></li>
</ul>
</div>