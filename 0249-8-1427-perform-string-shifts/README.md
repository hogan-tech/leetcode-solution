<h2> 249 8
1427. Perform String Shifts</h2><hr><div><p>You are given a string <code>s</code> containing lowercase English letters, and a matrix <code>shift</code>, where <code>shift[i] = [direction<sub>i</sub>, amount<sub>i</sub>]</code>:</p>

<ul>
	<li><code>direction<sub>i</sub></code> can be <code>0</code> (for left shift) or <code>1</code> (for right shift).</li>
	<li><code>amount<sub>i</sub></code> is the amount by which string <code>s</code> is to be shifted.</li>
	<li>A left shift by 1 means remove the first character of <code>s</code> and append it to the end.</li>
	<li>Similarly, a right shift by 1 means remove the last character of <code>s</code> and add it to the beginning.</li>
</ul>

<p>Return the final string after all operations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "abc", shift = [[0,1],[1,2]]
<strong>Output:</strong> "cab"
<strong>Explanation:</strong>&nbsp;
[0,1] means shift to left by 1. "abc" -&gt; "bca"
[1,2] means shift to right by 2. "bca" -&gt; "cab"</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
<strong>Output:</strong> "efgabcd"
<strong>Explanation:</strong>&nbsp; 
[1,1] means shift to right by 1. "abcdefg" -&gt; "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -&gt; "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -&gt; "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -&gt; "efgabcd"</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> only contains lower case English letters.</li>
	<li><code>1 &lt;= shift.length &lt;= 100</code></li>
	<li><code>shift[i].length == 2</code></li>
	<li><code>direction<sub>i</sub></code><sub> </sub>is either <code>0</code> or <code>1</code>.</li>
	<li><code>0 &lt;= amount<sub>i</sub> &lt;= 100</code></li>
</ul>
</div>