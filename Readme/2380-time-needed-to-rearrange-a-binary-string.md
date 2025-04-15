<h2><a href="https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string">2464. Time Needed to Rearrange a Binary String</a></h2><h3>Medium</h3><hr><p>You are given a binary string <code>s</code>. In one second, <strong>all</strong> occurrences of <code>&quot;01&quot;</code> are <strong>simultaneously</strong> replaced with <code>&quot;10&quot;</code>. This process <strong>repeats</strong> until no occurrences of <code>&quot;01&quot;</code> exist.</p>

<p>Return<em> the number of seconds needed to complete this process.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;0110101&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> 
After one second, s becomes &quot;1011010&quot;.
After another second, s becomes &quot;1101100&quot;.
After the third second, s becomes &quot;1110100&quot;.
After the fourth second, s becomes &quot;1111000&quot;.
No occurrence of &quot;01&quot; exists any longer, and the process needed 4 seconds to complete,
so we return 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;11100&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong>
No occurrence of &quot;01&quot; exists in s, and the processes needed 0 seconds to complete,
so we return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> is either <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<p>Can you solve this problem in O(n) time complexity?</p>
