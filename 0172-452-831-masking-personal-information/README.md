<h2> 172 452
831. Masking Personal Information</h2><hr><div><p>You are given a personal information string <code>s</code>, representing either an <strong>email address</strong> or a <strong>phone number</strong>. Return <em>the <strong>masked</strong> personal information using the below rules</em>.</p>

<p><u><strong>Email address:</strong></u></p>

<p>An email address is:</p>

<ul>
	<li>A <strong>name</strong> consisting of uppercase and lowercase English letters, followed by</li>
	<li>The <code>'@'</code> symbol, followed by</li>
	<li>The <strong>domain</strong> consisting of uppercase and lowercase English letters with a dot <code>'.'</code> somewhere in the middle (not the first or last character).</li>
</ul>

<p>To mask an email:</p>

<ul>
	<li>The uppercase letters in the <strong>name</strong> and <strong>domain</strong> must be converted to lowercase letters.</li>
	<li>The middle letters of the <strong>name</strong> (i.e., all but the first and last letters) must be replaced by 5 asterisks <code>"*****"</code>.</li>
</ul>

<p><u><strong>Phone number:</strong></u></p>

<p>A phone number is formatted as follows:</p>

<ul>
	<li>The phone number contains 10-13 digits.</li>
	<li>The last 10 digits make up the <strong>local number</strong>.</li>
	<li>The remaining 0-3 digits, in the beginning, make up the <strong>country code</strong>.</li>
	<li><strong>Separation characters</strong> from the set <code>{'+', '-', '(', ')', ' '}</code> separate the above digits in some way.</li>
</ul>

<p>To mask a phone number:</p>

<ul>
	<li>Remove all <strong>separation characters</strong>.</li>
	<li>The masked phone number should have the form:
	<ul>
		<li><code>"***-***-XXXX"</code> if the country code has 0 digits.</li>
		<li><code>"+*-***-***-XXXX"</code> if the country code has 1 digit.</li>
		<li><code>"+**-***-***-XXXX"</code> if the country code has 2 digits.</li>
		<li><code>"+***-***-***-XXXX"</code> if the country code has 3 digits.</li>
	</ul>
	</li>
	<li><code>"XXXX"</code> is the last 4 digits of the <strong>local number</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "LeetCode@LeetCode.com"
<strong>Output:</strong> "l*****e@leetcode.com"
<strong>Explanation:</strong> s is an email address.
The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "AB@qq.com"
<strong>Output:</strong> "a*****b@qq.com"
<strong>Explanation:</strong> s is an email address.
The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.
Note that even though "ab" is 2 characters, it still must have 5 asterisks in the middle.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "1(234)567-890"
<strong>Output:</strong> "***-***-7890"
<strong>Explanation:</strong> s is a phone number.
There are 10 digits, so the local number is 10 digits and the country code is 0 digits.
Thus, the resulting masked number is "***-***-7890".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>s</code> is either a <strong>valid</strong> email or a phone number.</li>
	<li>If <code>s</code> is an email:
	<ul>
		<li><code>8 &lt;= s.length &lt;= 40</code></li>
		<li><code>s</code> consists of uppercase and lowercase English letters and exactly one <code>'@'</code> symbol and <code>'.'</code> symbol.</li>
	</ul>
	</li>
	<li>If <code>s</code> is a phone number:
	<ul>
		<li><code>10 &lt;= s.length &lt;= 20</code></li>
		<li><code>s</code> consists of digits, spaces, and the symbols <code>'('</code>, <code>')'</code>, <code>'-'</code>, and <code>'+'</code>.</li>
	</ul>
	</li>
</ul>
</div>