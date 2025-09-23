<h2><a href="https://leetcode.com/problems/compare-version-numbers">165. Compare Version Numbers</a></h2><h3>Medium</h3><hr><p>Given two <strong>version strings</strong>, <code>version1</code> and <code>version2</code>, compare them. A version string consists of <strong>revisions</strong> separated by dots <code>&#39;.&#39;</code>. The <strong>value of the revision</strong> is its <strong>integer conversion</strong> ignoring leading zeros.</p>

<p>To compare version strings, compare their revision values in <strong>left-to-right order</strong>. If one of the version strings has fewer revisions, treat the missing revision values as <code>0</code>.</p>

<p>Return the following:</p>

<ul>
	<li>If <code>version1 &lt; version2</code>, return -1.</li>
	<li>If <code>version1 &gt; version2</code>, return 1.</li>
	<li>Otherwise, return 0.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">version1 = &quot;1.2&quot;, version2 = &quot;1.10&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>version1&#39;s second revision is &quot;2&quot; and version2&#39;s second revision is &quot;10&quot;: 2 &lt; 10, so version1 &lt; version2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">version1 = &quot;1.01&quot;, version2 = &quot;1.001&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>Ignoring leading zeroes, both &quot;01&quot; and &quot;001&quot; represent the same integer &quot;1&quot;.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">version1 = &quot;1.0&quot;, version2 = &quot;1.0.0.0&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>version1 has less revisions, which means every missing revision are treated as &quot;0&quot;.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= version1.length, version2.length &lt;= 500</code></li>
	<li><code>version1</code> and <code>version2</code>&nbsp;only contain digits and <code>&#39;.&#39;</code>.</li>
	<li><code>version1</code> and <code>version2</code>&nbsp;<strong>are valid version numbers</strong>.</li>
	<li>All the given revisions in&nbsp;<code>version1</code> and <code>version2</code>&nbsp;can be stored in&nbsp;a&nbsp;<strong>32-bit integer</strong>.</li>
</ul>
