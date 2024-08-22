<h2><a href="https://leetcode.com/problems/generalized-abbreviation/">320. Generalized Abbreviation</a></h2><h3>Medium</h3><hr><div><p>A word's <strong>generalized abbreviation</strong> can be constructed by taking any number of <strong>non-overlapping</strong> and <strong>non-adjacent</strong> <span data-keyword="substring-nonempty">substrings</span> and replacing them with their respective lengths.</p>

<ul>
	<li>For example, <code>"abcde"</code> can be abbreviated into:

	<ul>
		<li><code>"a3e"</code> (<code>"bcd"</code> turned into <code>"3"</code>)</li>
		<li><code>"1bcd1"</code> (<code>"a"</code> and <code>"e"</code> both turned into <code>"1"</code>)</li>
		<li><code>"5"</code> (<code>"abcde"</code> turned into <code>"5"</code>)</li>
		<li><code>"abcde"</code> (no substrings replaced)</li>
	</ul>
	</li>
	<li>However, these abbreviations are <strong>invalid</strong>:
	<ul>
		<li><code>"23"</code> (<code>"ab"</code> turned into <code>"2"</code> and <code>"cde"</code> turned into <code>"3"</code>) is invalid as the substrings chosen are adjacent.</li>
		<li><code>"22de"</code> (<code>"ab"</code> turned into <code>"2"</code> and <code>"bc"</code> turned into <code>"2"</code>) is invalid as the substring chosen overlap.</li>
	</ul>
	</li>
</ul>

<p>Given a string <code>word</code>, return <em>a list of all the possible <strong>generalized abbreviations</strong> of</em> <code>word</code>. Return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> word = "word"
<strong>Output:</strong> ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> word = "a"
<strong>Output:</strong> ["1","a"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 15</code></li>
	<li><code>word</code> consists of only lowercase English letters.</li>
</ul>
</div>