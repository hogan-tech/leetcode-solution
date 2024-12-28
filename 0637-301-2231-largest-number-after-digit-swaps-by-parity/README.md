<h2> 637 301
2231. Largest Number After Digit Swaps by Parity</h2><hr><div><p>You are given a positive integer <code>num</code>. You may swap any two digits of <code>num</code> that have the same <strong>parity</strong> (i.e. both odd digits or both even digits).</p>

<p>Return<em> the <strong>largest</strong> possible value of </em><code>num</code><em> after <strong>any</strong> number of swaps.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> num = 1234
<strong>Output:</strong> 3412
<strong>Explanation:</strong> Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> num = 65875
<strong>Output:</strong> 87655
<strong>Explanation:</strong> Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 10<sup>9</sup></code></li>
</ul>
</div>