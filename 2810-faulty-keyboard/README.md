<h2><a href="https://leetcode.com/problems/faulty-keyboard/">2810. Faulty Keyboard</a></h2><h3>Easy</h3><hr><div><p>Your laptop keyboard is faulty, and whenever you type a character <code>'i'</code> on it, it reverses the string that you have written. Typing other characters works as expected.</p>

<p>You are given a <strong>0-indexed</strong> string <code>s</code>, and you type each character of <code>s</code> using your faulty keyboard.</p>

<p>Return <em>the final string that will be present on your laptop screen.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "string"
<strong>Output:</strong> "rtsng"
<strong>Explanation:</strong> 
After typing first character, the text on the screen is "s".
After the second character, the text is "st". 
After the third character, the text is "str".
Since the fourth character is an 'i', the text gets reversed and becomes "rts".
After the fifth character, the text is "rtsn". 
After the sixth character, the text is "rtsng". 
Therefore, we return "rtsng".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "poiinter"
<strong>Output:</strong> "ponter"
<strong>Explanation:</strong> 
After the first character, the text on the screen is "p".
After the second character, the text is "po". 
Since the third character you type is an 'i', the text gets reversed and becomes "op". 
Since the fourth character you type is an 'i', the text gets reversed and becomes "po".
After the fifth character, the text is "pon".
After the sixth character, the text is "pont". 
After the seventh character, the text is "ponte". 
After the eighth character, the text is "ponter". 
Therefore, we return "ponter".</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>s[0] != 'i'</code></li>
</ul>
</div>