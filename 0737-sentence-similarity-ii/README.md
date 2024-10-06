<h2><a href="https://leetcode.com/problems/sentence-similarity-ii/">737. Sentence Similarity II</a></h2><h3>Medium</h3><hr><div><p>We can represent a sentence as an array of words, for example, the sentence <code>"I am happy with leetcode"</code> can be represented as <code>arr = ["I","am",happy","with","leetcode"]</code>.</p>

<p>Given two sentences <code>sentence1</code> and <code>sentence2</code> each represented as a string array and given an array of string pairs <code>similarPairs</code> where <code>similarPairs[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> indicates that the two words <code>x<sub>i</sub></code> and <code>y<sub>i</sub></code> are similar.</p>

<p>Return <code>true</code><em> if <code>sentence1</code> and <code>sentence2</code> are similar, or </em><code>false</code><em> if they are not similar</em>.</p>

<p>Two sentences are similar if:</p>

<ul>
	<li>They have <strong>the same length</strong> (i.e., the same number of words)</li>
	<li><code>sentence1[i]</code> and <code>sentence2[i]</code> are similar.</li>
</ul>

<p>Notice that a word is always similar to itself, also notice that the similarity relation is transitive. For example, if the words <code>a</code> and <code>b</code> are similar, and the words <code>b</code> and <code>c</code> are similar, then&nbsp;<code>a</code> and <code>c</code> are <strong>similar</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
<strong>Output:</strong> true
<strong>Explanation:</strong> The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
<strong>Output:</strong> true
<strong>Explanation:</strong> "leetcode" --&gt; "platform" --&gt; "anime" --&gt; "manga" --&gt; "onepiece".
Since "leetcode is similar to "onepiece" and the first two words are the same, the two sentences are similar.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]
<strong>Output:</strong> false
<strong>Explanation:</strong> "leetcode" is not similar to "onepiece".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sentence1.length, sentence2.length &lt;= 1000</code></li>
	<li><code>1 &lt;= sentence1[i].length, sentence2[i].length &lt;= 20</code></li>
	<li><code>sentence1[i]</code> and <code>sentence2[i]</code> consist of lower-case and upper-case English letters.</li>
	<li><code>0 &lt;= similarPairs.length &lt;= 2000</code></li>
	<li><code>similarPairs[i].length == 2</code></li>
	<li><code>1 &lt;= x<sub>i</sub>.length, y<sub>i</sub>.length &lt;= 20</code></li>
	<li><code>x<sub>i</sub></code> and <code>y<sub>i</sub></code> consist of English letters.</li>
</ul>
</div>