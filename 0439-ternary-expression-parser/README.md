<h2><a href="https://leetcode.com/problems/ternary-expression-parser/">439. Ternary Expression Parser</a></h2><h3>Medium</h3><hr><div><p>Given a string <code>expression</code> representing arbitrarily nested ternary expressions, evaluate the expression, and return <em>the result of it</em>.</p>

<p>You can always assume that the given expression is valid and only contains digits, <code>'?'</code>, <code>':'</code>, <code>'T'</code>, and <code>'F'</code> where <code>'T'</code> is true and <code>'F'</code> is false. All the numbers in the expression are <strong>one-digit</strong> numbers (i.e., in the range <code>[0, 9]</code>).</p>

<p>The conditional expressions group right-to-left (as usual in most languages), and the result of the expression will always evaluate to either a digit, <code>'T'</code> or <code>'F'</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> expression = "T?2:3"
<strong>Output:</strong> "2"
<strong>Explanation:</strong> If true, then result is 2; otherwise result is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> expression = "F?1:T?4:5"
<strong>Output:</strong> "4"
<strong>Explanation:</strong> The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
"(F ? 1 : (T ? 4 : 5))" --&gt; "(F ? 1 : 4)" --&gt; "4"
or "(F ? 1 : (T ? 4 : 5))" --&gt; "(T ? 4 : 5)" --&gt; "4"
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> expression = "T?T?F:5:3"
<strong>Output:</strong> "F"
<strong>Explanation:</strong> The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
"(T ? (T ? F : 5) : 3)" --&gt; "(T ? F : 3)" --&gt; "F"
"(T ? (T ? F : 5) : 3)" --&gt; "(T ? F : 5)" --&gt; "F"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>5 &lt;= expression.length &lt;= 10<sup>4</sup></code></li>
	<li><code>expression</code> consists of digits, <code>'T'</code>, <code>'F'</code>, <code>'?'</code>, and <code>':'</code>.</li>
	<li>It is <strong>guaranteed</strong> that <code>expression</code> is a valid ternary expression and that each number is a <strong>one-digit number</strong>.</li>
</ul>
</div>