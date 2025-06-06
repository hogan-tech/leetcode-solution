<h2><a href="https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string">2520. Using a Robot to Print the Lexicographically Smallest String</a></h2><h3>Medium</h3><hr><p>You are given a string <code>s</code> and a robot that currently holds an empty string <code>t</code>. Apply one of the following operations until <code>s</code> and <code>t</code> <strong>are both empty</strong>:</p>

<ul>
	<li>Remove the <strong>first</strong> character of a string <code>s</code> and give it to the robot. The robot will append this character to the string <code>t</code>.</li>
	<li>Remove the <strong>last</strong> character of a string <code>t</code> and give it to the robot. The robot will write this character on paper.</li>
</ul>

<p>Return <em>the lexicographically smallest string that can be written on the paper.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;zza&quot;
<strong>Output:</strong> &quot;azz&quot;
<strong>Explanation:</strong> Let p denote the written string.
Initially p=&quot;&quot;, s=&quot;zza&quot;, t=&quot;&quot;.
Perform first operation three times p=&quot;&quot;, s=&quot;&quot;, t=&quot;zza&quot;.
Perform second operation three times p=&quot;azz&quot;, s=&quot;&quot;, t=&quot;&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bac&quot;
<strong>Output:</strong> &quot;abc&quot;
<strong>Explanation:</strong> Let p denote the written string.
Perform first operation twice p=&quot;&quot;, s=&quot;c&quot;, t=&quot;ba&quot;. 
Perform second operation twice p=&quot;ab&quot;, s=&quot;c&quot;, t=&quot;&quot;. 
Perform first operation p=&quot;ab&quot;, s=&quot;&quot;, t=&quot;c&quot;. 
Perform second operation p=&quot;abc&quot;, s=&quot;&quot;, t=&quot;&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bdda&quot;
<strong>Output:</strong> &quot;addb&quot;
<strong>Explanation:</strong> Let p denote the written string.
Initially p=&quot;&quot;, s=&quot;bdda&quot;, t=&quot;&quot;.
Perform first operation four times p=&quot;&quot;, s=&quot;&quot;, t=&quot;bdda&quot;.
Perform second operation four times p=&quot;addb&quot;, s=&quot;&quot;, t=&quot;&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only English lowercase letters.</li>
</ul>
