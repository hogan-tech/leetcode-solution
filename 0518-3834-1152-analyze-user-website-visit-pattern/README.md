<h2> 518 3834
1152. Analyze User Website Visit Pattern</h2><hr><div><p>You are given two string arrays <code>username</code> and <code>website</code> and an integer array <code>timestamp</code>. All the given arrays are of the same length and the tuple <code>[username[i], website[i], timestamp[i]]</code> indicates that the user <code>username[i]</code> visited the website <code>website[i]</code> at time <code>timestamp[i]</code>.</p>

<p>A <strong>pattern</strong> is a list of three websites (not necessarily distinct).</p>

<ul>
	<li>For example, <code>["home", "away", "love"]</code>, <code>["leetcode", "love", "leetcode"]</code>, and <code>["luffy", "luffy", "luffy"]</code> are all patterns.</li>
</ul>

<p>The <strong>score</strong> of a <strong>pattern</strong> is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.</p>

<ul>
	<li>For example, if the pattern is <code>["home", "away", "love"]</code>, the score is the number of users <code>x</code> such that <code>x</code> visited <code>"home"</code> then visited <code>"away"</code> and visited <code>"love"</code> after that.</li>
	<li>Similarly, if the pattern is <code>["leetcode", "love", "leetcode"]</code>, the score is the number of users <code>x</code> such that <code>x</code> visited <code>"leetcode"</code> then visited <code>"love"</code> and visited <code>"leetcode"</code> <strong>one more time</strong> after that.</li>
	<li>Also, if the pattern is <code>["luffy", "luffy", "luffy"]</code>, the score is the number of users <code>x</code> such that <code>x</code> visited <code>"luffy"</code> three different times at different timestamps.</li>
</ul>

<p>Return the <strong>pattern</strong> with the largest <strong>score</strong>. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.</p>

<p>Note that the websites in a pattern <strong>do not</strong> need to be visited <em>contiguously</em>, they only need to be visited in the order they appeared in the pattern.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
<strong>Output:</strong> ["home","about","career"]
<strong>Explanation:</strong> The tuples in this example are:
["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
The pattern ("home", "about", "career") has score 2 (joe and mary).
The pattern ("home", "cart", "maps") has score 1 (james).
The pattern ("home", "cart", "home") has score 1 (james).
The pattern ("home", "maps", "home") has score 1 (james).
The pattern ("cart", "maps", "home") has score 1 (james).
The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]
<strong>Output:</strong> ["a","b","a"]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= username.length &lt;= 50</code></li>
	<li><code>1 &lt;= username[i].length &lt;= 10</code></li>
	<li><code>timestamp.length == username.length</code></li>
	<li><code>1 &lt;= timestamp[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>website.length == username.length</code></li>
	<li><code>1 &lt;= website[i].length &lt;= 10</code></li>
	<li><code>username[i]</code> and <code>website[i]</code> consist of lowercase English letters.</li>
	<li>It is guaranteed that there is at least one user who visited at least three websites.</li>
	<li>All the tuples <code>[username[i], timestamp[i], website[i]]</code> are <strong>unique</strong>.</li>
</ul>
</div>