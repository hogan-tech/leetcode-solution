<h2> 223 229
1946. Largest Number After Mutating Substring</h2><hr><div><p>You are given a string <code>num</code>, which represents a large integer. You are also given a <strong>0-indexed</strong> integer array <code>change</code> of length <code>10</code> that maps each digit <code>0-9</code> to another digit. More formally, digit <code>d</code> maps to digit <code>change[d]</code>.</p>

<p>You may <strong>choose</strong> to <b>mutate a single substring</b> of <code>num</code>. To mutate a substring, replace each digit <code>num[i]</code> with the digit it maps to in <code>change</code> (i.e. replace <code>num[i]</code> with <code>change[num[i]]</code>).</p>

<p>Return <em>a string representing the <strong>largest</strong> possible integer after <strong>mutating</strong> (or choosing not to) a <strong>single substring</strong> of </em><code>num</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within the string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> num = "<u>1</u>32", change = [9,8,5,0,3,6,4,2,6,8]
<strong>Output:</strong> "<u>8</u>32"
<strong>Explanation:</strong> Replace the substring "1":
- 1 maps to change[1] = 8.
Thus, "<u>1</u>32" becomes "<u>8</u>32".
"832" is the largest number that can be created, so return it.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> num = "<u>021</u>", change = [9,4,3,5,7,2,1,9,0,6]
<strong>Output:</strong> "<u>934</u>"
<strong>Explanation:</strong> Replace the substring "021":
- 0 maps to change[0] = 9.
- 2 maps to change[2] = 3.
- 1 maps to change[1] = 4.
Thus, "<u>021</u>" becomes "<u>934</u>".
"934" is the largest number that can be created, so return it.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> num = "5", change = [1,4,7,5,3,2,5,6,9,4]
<strong>Output:</strong> "5"
<strong>Explanation:</strong> "5" is already the largest number that can be created, so return it.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 10<sup>5</sup></code></li>
	<li><code>num</code> consists of only digits <code>0-9</code>.</li>
	<li><code>change.length == 10</code></li>
	<li><code>0 &lt;= change[d] &lt;= 9</code></li>
</ul>
</div>