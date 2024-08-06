<h2><a href="https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/">3016. Minimum Number of Pushes to Type Word II</a></h2><h3>Medium</h3><hr><div><p>You are given a string <code>word</code> containing lowercase English letters.</p>

<p>Telephone keypads have keys mapped with <strong>distinct</strong> collections of lowercase English letters, which can be used to form words by pushing them. For example, the key <code>2</code> is mapped with <code>["a","b","c"]</code>, we need to push the key one time to type <code>"a"</code>, two times to type <code>"b"</code>, and three times to type <code>"c"</code> <em>.</em></p>

<p>It is allowed to remap the keys numbered <code>2</code> to <code>9</code> to <strong>distinct</strong> collections of letters. The keys can be remapped to <strong>any</strong> amount of letters, but each letter <strong>must</strong> be mapped to <strong>exactly</strong> one key. You need to find the <strong>minimum</strong> number of times the keys will be pushed to type the string <code>word</code>.</p>

<p>Return <em>the <strong>minimum</strong> number of pushes needed to type </em><code>word</code> <em>after remapping the keys</em>.</p>

<p>An example mapping of letters to keys on a telephone keypad is given below. Note that <code>1</code>, <code>*</code>, <code>#</code>, and <code>0</code> do <strong>not</strong> map to any letters.</p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypaddesc.png" style="width: 329px; height: 313px;">
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypadv1e1.png" style="width: 329px; height: 313px;">
<pre><strong>Input:</strong> word = "abcde"
<strong>Output:</strong> 5
<strong>Explanation:</strong> The remapped keypad given in the image provides the minimum cost.
"a" -&gt; one push on key 2
"b" -&gt; one push on key 3
"c" -&gt; one push on key 4
"d" -&gt; one push on key 5
"e" -&gt; one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/26/keypadv2e2.png" style="width: 329px; height: 313px;">
<pre><strong>Input:</strong> word = "xyzxyzxyzxyz"
<strong>Output:</strong> 12
<strong>Explanation:</strong> The remapped keypad given in the image provides the minimum cost.
"x" -&gt; one push on key 2
"y" -&gt; one push on key 3
"z" -&gt; one push on key 4
Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
It can be shown that no other mapping can provide a lower cost.
Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/27/keypadv2.png" style="width: 329px; height: 313px;">
<pre><strong>Input:</strong> word = "aabbccddeeffgghhiiiiii"
<strong>Output:</strong> 24
<strong>Explanation:</strong> The remapped keypad given in the image provides the minimum cost.
"a" -&gt; one push on key 2
"b" -&gt; one push on key 3
"c" -&gt; one push on key 4
"d" -&gt; one push on key 5
"e" -&gt; one push on key 6
"f" -&gt; one push on key 7
"g" -&gt; one push on key 8
"h" -&gt; two pushes on key 9
"i" -&gt; one push on key 9
Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.
It can be shown that no other mapping can provide a lower cost.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 10<sup>5</sup></code></li>
	<li><code>word</code> consists of lowercase English letters.</li>
</ul>
</div>