<h2><a href="https://leetcode.com/problems/rle-iterator">936. RLE Iterator</a></h2><h3>Medium</h3><hr><p>We can use run-length encoding (i.e., <strong>RLE</strong>) to encode a sequence of integers. In a run-length encoded array of even length <code>encoding</code> (<strong>0-indexed</strong>), for all even <code>i</code>, <code>encoding[i]</code> tells us the number of times that the non-negative integer value <code>encoding[i + 1]</code> is repeated in the sequence.</p>

<ul>
	<li>For example, the sequence <code>arr = [8,8,8,5,5]</code> can be encoded to be <code>encoding = [3,8,2,5]</code>. <code>encoding = [3,8,0,9,2,5]</code> and <code>encoding = [2,8,1,8,2,5]</code> are also valid <strong>RLE</strong> of <code>arr</code>.</li>
</ul>

<p>Given a run-length encoded array, design an iterator that iterates through it.</p>

<p>Implement the <code>RLEIterator</code> class:</p>

<ul>
	<li><code>RLEIterator(int[] encoded)</code> Initializes the object with the encoded array <code>encoded</code>.</li>
	<li><code>int next(int n)</code> Exhausts the next <code>n</code> elements and returns the last element exhausted in this way. If there is no element left to exhaust, return <code>-1</code> instead.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;RLEIterator&quot;, &quot;next&quot;, &quot;next&quot;, &quot;next&quot;, &quot;next&quot;]
[[[3, 8, 0, 9, 2, 5]], [2], [1], [1], [2]]
<strong>Output</strong>
[null, 8, 8, 5, -1]

<strong>Explanation</strong>
RLEIterator rLEIterator = new RLEIterator([3, 8, 0, 9, 2, 5]); // This maps to the sequence [8,8,8,5,5].
rLEIterator.next(2); // exhausts 2 terms of the sequence, returning 8. The remaining sequence is now [8, 5, 5].
rLEIterator.next(1); // exhausts 1 term of the sequence, returning 8. The remaining sequence is now [5, 5].
rLEIterator.next(1); // exhausts 1 term of the sequence, returning 5. The remaining sequence is now [5].
rLEIterator.next(2); // exhausts 2 terms, returning -1. This is because the first term exhausted was 5,
but the second term did not exist. Since the last term exhausted does not exist, we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= encoding.length &lt;= 1000</code></li>
	<li><code>encoding.length</code> is even.</li>
	<li><code>0 &lt;= encoding[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li>At most <code>1000</code> calls will be made to <code>next</code>.</li>
</ul>
