<h2><a href="https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string">1934. Evaluate the Bracket Pairs of a String</a></h2><h3>Medium</h3><hr><p>You are given a string <code>s</code> that contains some bracket pairs, with each pair containing a <strong>non-empty</strong> key.</p>

<ul>
	<li>For example, in the string <code>&quot;(name)is(age)yearsold&quot;</code>, there are <strong>two</strong> bracket pairs that contain the keys <code>&quot;name&quot;</code> and <code>&quot;age&quot;</code>.</li>
</ul>

<p>You know the values of a wide range of keys. This is represented by a 2D string array <code>knowledge</code> where each <code>knowledge[i] = [key<sub>i</sub>, value<sub>i</sub>]</code> indicates that key <code>key<sub>i</sub></code> has a value of <code>value<sub>i</sub></code>.</p>

<p>You are tasked to evaluate <strong>all</strong> of the bracket pairs. When you evaluate a bracket pair that contains some key <code>key<sub>i</sub></code>, you will:</p>

<ul>
	<li>Replace <code>key<sub>i</sub></code> and the bracket pair with the key&#39;s corresponding <code>value<sub>i</sub></code>.</li>
	<li>If you do not know the value of the key, you will replace <code>key<sub>i</sub></code> and the bracket pair with a question mark <code>&quot;?&quot;</code> (without the quotation marks).</li>
</ul>

<p>Each key will appear at most once in your <code>knowledge</code>. There will not be any nested brackets in <code>s</code>.</p>

<p>Return <em>the resulting string after evaluating <strong>all</strong> of the bracket pairs.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(name)is(age)yearsold&quot;, knowledge = [[&quot;name&quot;,&quot;bob&quot;],[&quot;age&quot;,&quot;two&quot;]]
<strong>Output:</strong> &quot;bobistwoyearsold&quot;
<strong>Explanation:</strong>
The key &quot;name&quot; has a value of &quot;bob&quot;, so replace &quot;(name)&quot; with &quot;bob&quot;.
The key &quot;age&quot; has a value of &quot;two&quot;, so replace &quot;(age)&quot; with &quot;two&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;hi(name)&quot;, knowledge = [[&quot;a&quot;,&quot;b&quot;]]
<strong>Output:</strong> &quot;hi?&quot;
<strong>Explanation:</strong> As you do not know the value of the key &quot;name&quot;, replace &quot;(name)&quot; with &quot;?&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(a)(a)(a)aaa&quot;, knowledge = [[&quot;a&quot;,&quot;yes&quot;]]
<strong>Output:</strong> &quot;yesyesyesaaa&quot;
<strong>Explanation:</strong> The same key can appear multiple times.
The key &quot;a&quot; has a value of &quot;yes&quot;, so replace all occurrences of &quot;(a)&quot; with &quot;yes&quot;.
Notice that the &quot;a&quot;s not in a bracket pair are not evaluated.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= knowledge.length &lt;= 10<sup>5</sup></code></li>
	<li><code>knowledge[i].length == 2</code></li>
	<li><code>1 &lt;= key<sub>i</sub>.length, value<sub>i</sub>.length &lt;= 10</code></li>
	<li><code>s</code> consists of lowercase English letters and round brackets <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>.</li>
	<li>Every open bracket <code>&#39;(&#39;</code> in <code>s</code> will have a corresponding close bracket <code>&#39;)&#39;</code>.</li>
	<li>The key in each bracket pair of <code>s</code> will be non-empty.</li>
	<li>There will not be any nested bracket pairs in <code>s</code>.</li>
	<li><code>key<sub>i</sub></code> and <code>value<sub>i</sub></code> consist of lowercase English letters.</li>
	<li>Each <code>key<sub>i</sub></code> in <code>knowledge</code> is unique.</li>
</ul>
