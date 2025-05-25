<h2><a href="https://leetcode.com/problems/sum-of-largest-prime-substrings">3815. Sum of Largest Prime Substrings</a></h2><h3>Medium</h3><hr><p data-end="157" data-start="30">Given a string <code>s</code>, find the sum of the <strong>3 largest unique prime numbers</strong> that can be formed using any of its<strong> substrings</strong>.</p>

<p data-end="269" data-start="166">Return the <strong>sum</strong> of the three largest unique prime numbers that can be formed. If fewer than three exist, return the sum of <strong>all</strong> available primes. If no prime numbers can be formed, return 0.</p>

<p data-end="269" data-start="166">A prime number is a natural number greater than 1 with only two factors, 1 and itself.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within a string.</p>

<p data-end="370" data-is-last-node="" data-is-only-node="" data-start="271"><strong data-end="280" data-start="271">Note:</strong> Each prime number should be counted only <strong>once</strong>, even if it appears in <strong>multiple</strong> substrings. Additionally, when converting a substring to an integer, any leading zeros are ignored.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;12234&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">1469</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li data-end="136" data-start="16">The unique prime numbers formed from the substrings of <code>&quot;12234&quot;</code> are 2, 3, 23, 223, and 1223.</li>
	<li data-end="226" data-start="137">The 3 largest primes are 1223, 223, and 23. Their sum is 1469.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;111&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">11</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li data-end="339" data-start="244">The unique prime number formed from the substrings of <code>&quot;111&quot;</code> is 11.</li>
	<li data-end="412" data-is-last-node="" data-start="340">Since there is only one prime number, the sum is 11.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li data-end="39" data-start="18"><code>1 &lt;= s.length &lt;= 10</code></li>
	<li data-end="68" data-is-last-node="" data-start="40"><code>s</code> consists of only digits.</li>
</ul>
