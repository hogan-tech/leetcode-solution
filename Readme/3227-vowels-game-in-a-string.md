<h2> 141 36
3227. Vowels Game in a String</h2><hr><div><p>Alice and Bob are playing a game on a string.</p>

<p>You are given a string <code>s</code>, Alice and Bob will take turns playing the following game where Alice starts <strong>first</strong>:</p>

<ul>
	<li>On Alice's turn, she has to remove any <strong>non-empty</strong> <span data-keyword="substring">substring</span> from <code>s</code> that contains an <strong>odd</strong> number of vowels.</li>
	<li>On Bob's turn, he has to remove any <strong>non-empty</strong> <span data-keyword="substring">substring</span> from <code>s</code> that contains an <strong>even</strong> number of vowels.</li>
</ul>

<p>The first player who cannot make a move on their turn loses the game. We assume that both Alice and Bob play <strong>optimally</strong>.</p>

<p>Return <code>true</code> if Alice wins the game, and <code>false</code> otherwise.</p>

<p>The English vowels are: <code>a</code>, <code>e</code>, <code>i</code>, <code>o</code>, and <code>u</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "leetcoder"</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong><br>
Alice can win the game as follows:</p>

<ul>
	<li>Alice plays first, she can delete the underlined substring in <code>s = "<u><strong>leetco</strong></u>der"</code> which contains 3 vowels. The resulting string is <code>s = "der"</code>.</li>
	<li>Bob plays second, he can delete the underlined substring in <code>s = "<u><strong>d</strong></u>er"</code> which contains 0 vowels. The resulting string is <code>s = "er"</code>.</li>
	<li>Alice plays third, she can delete the whole string <code>s = "<strong><u>er</u></strong>"</code> which contains 1 vowel.</li>
	<li>Bob plays fourth, since the string is empty, there is no valid play for Bob. So Alice wins the game.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = "bbcd"</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong><br>
There is no valid play for Alice in her first turn, so Alice loses the game.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>
</div>