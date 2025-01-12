<h2> 1067 360
244. Shortest Word Distance II</h2><hr><div><p>Design a data structure that will be initialized with a string array, and then it should answer queries of the shortest distance between two different strings from the array.</p>

<p>Implement the <code>WordDistance</code> class:</p>

<ul>
	<li><code>WordDistance(String[] wordsDict)</code> initializes the object with the strings array <code>wordsDict</code>.</li>
	<li><code>int shortest(String word1, String word2)</code> returns the shortest distance between <code>word1</code> and <code>word2</code> in the array <code>wordsDict</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input</strong>
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
<strong>Output</strong>
[null, 3, 1]

<strong>Explanation</strong>
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= wordsDict.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= wordsDict[i].length &lt;= 10</code></li>
	<li><code>wordsDict[i]</code> consists of lowercase English letters.</li>
	<li><code>word1</code> and <code>word2</code> are in <code>wordsDict</code>.</li>
	<li><code>word1 != word2</code></li>
	<li>At most <code>5000</code> calls will be made to <code>shortest</code>.</li>
</ul>
</div>