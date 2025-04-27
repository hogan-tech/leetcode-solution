<h2><a href="https://leetcode.com/problems/find-the-most-common-response">3707. Find the Most Common Response</a></h2><h3>Medium</h3><hr><p>You are given a 2D string array <code>responses</code> where each <code>responses[i]</code> is an array of strings representing survey responses from the <code>i<sup>th</sup></code> day.</p>

<p>Return the <strong>most common</strong> response across all days after removing <strong>duplicate</strong> responses within each <code>responses[i]</code>. If there is a tie, return the <em>lexicographically smallest</em> response.</p>
A string <code>a</code> is <strong>lexicographically smaller</strong> than a string <code>b</code> if in the first position where <code>a</code> and <code>b</code> differ, string <code>a</code> has a letter that appears earlier in the alphabet than the corresponding letter in <code>b</code>.<br />
If the first <code>min(a.length, b.length)</code> characters do not differ, then the shorter string is the lexicographically smaller one.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">responses = [[&quot;good&quot;,&quot;ok&quot;,&quot;good&quot;,&quot;ok&quot;],[&quot;ok&quot;,&quot;bad&quot;,&quot;good&quot;,&quot;ok&quot;,&quot;ok&quot;],[&quot;good&quot;],[&quot;bad&quot;]]</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;good&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>After removing duplicates within each list, <code>responses = [[&quot;good&quot;, &quot;ok&quot;], [&quot;ok&quot;, &quot;bad&quot;, &quot;good&quot;], [&quot;good&quot;], [&quot;bad&quot;]]</code>.</li>
	<li><code>&quot;good&quot;</code> appears 3 times, <code>&quot;ok&quot;</code> appears 2 times, and <code>&quot;bad&quot;</code> appears 2 times.</li>
	<li>Return <code>&quot;good&quot;</code> because it has the highest frequency.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">responses = [[&quot;good&quot;,&quot;ok&quot;,&quot;good&quot;],[&quot;ok&quot;,&quot;bad&quot;],[&quot;bad&quot;,&quot;notsure&quot;],[&quot;great&quot;,&quot;good&quot;]]</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;bad&quot;</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>After removing duplicates within each list we have <code>responses = [[&quot;good&quot;, &quot;ok&quot;], [&quot;ok&quot;, &quot;bad&quot;], [&quot;bad&quot;, &quot;notsure&quot;], [&quot;great&quot;, &quot;good&quot;]]</code>.</li>
	<li><code>&quot;bad&quot;</code>, <code>&quot;good&quot;</code>, and <code>&quot;ok&quot;</code> each occur 2 times.</li>
	<li>The output is <code>&quot;bad&quot;</code> because it is the lexicographically smallest amongst the words with the highest frequency.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= responses.length &lt;= 1000</code></li>
	<li><code>1 &lt;= responses[i].length &lt;= 1000</code></li>
	<li><code>1 &lt;= responses[i][j].length &lt;= 10</code></li>
	<li><code>responses[i][j]</code> consists of only lowercase English letters</li>
</ul>
