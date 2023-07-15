<h2><a href="https://leetcode.com/problems/promise-time-limit/">2637. Promise Time Limit</a></h2><h3>Easy</h3><hr><div><p>Given an&nbsp;asynchronous function&nbsp;<code>fn</code>&nbsp;and a time <code>t</code>&nbsp;in milliseconds, return&nbsp;a new&nbsp;<strong>time limited</strong>&nbsp;version of the input function. <code>fn</code> takes arguments provided to the&nbsp;<strong>time limited&nbsp;</strong>function.</p>

<p>The <strong>time limited</strong> function should follow these rules:</p>

<ul>
	<li>If the <code>fn</code> completes within the time limit of <code>t</code> milliseconds, the <strong>time limited</strong> function should&nbsp;resolve with the result.</li>
	<li>If the execution of the <code>fn</code> exceeds the time limit, the <strong>time limited</strong> function should reject with the string <code>"Time Limit Exceeded"</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> 
fn = async (n) =&gt; { 
&nbsp; await new Promise(res =&gt; setTimeout(res, 100)); 
&nbsp; return n * n; 
}
inputs = [5]
t = 50
<strong>Output:</strong> {"rejected":"Time Limit Exceeded","time":50}
<strong>Explanation:</strong>
const limited = timeLimit(fn, t)
const start = performance.now()
let result;
try {
&nbsp; &nbsp;const res = await limited(...inputs)
&nbsp; &nbsp;result = {"resolved": res, "time": Math.floor(performance.now() - start)};
} catch (err) {
&nbsp;  result = {"rejected": err, "time": Math.floor(performance.now() - start)};
}
console.log(result) // Output

The provided function is set to resolve after 100ms. However, the time limit is set to 50ms. It rejects at t=50ms because the time limit was reached.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> 
fn = async (n) =&gt; { 
&nbsp; await new Promise(res =&gt; setTimeout(res, 100)); 
&nbsp; return n * n; 
}
inputs = [5]
t = 150
<strong>Output:</strong> {"resolved":25,"time":100}
<strong>Explanation:</strong>
The function resolved 5 * 5 = 25 at t=100ms. The time limit is never reached.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> 
fn = async (a, b) =&gt; { 
&nbsp; await new Promise(res =&gt; setTimeout(res, 120)); 
&nbsp; return a + b; 
}
inputs = [5,10]
t = 150
<strong>Output:</strong> {"resolved":15,"time":120}
<strong>Explanation:</strong>
​​​​The function resolved 5 + 10 = 15 at t=120ms. The time limit is never reached.
</pre>

<p><strong class="example">Example 4:</strong></p>

<pre><strong>Input:</strong> 
fn = async () =&gt; { 
&nbsp; throw "Error";
}
inputs = []
t = 1000
<strong>Output:</strong> {"rejected":"Error","time":0}
<strong>Explanation:</strong>
The function immediately throws an error.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= inputs.length &lt;= 10</code></li>
	<li><code>0 &lt;= t &lt;= 1000</code></li>
	<li><code>fn returns a promise</code></li>
</ul>
</div>