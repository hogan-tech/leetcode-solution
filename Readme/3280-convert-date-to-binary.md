<h2><a href="https://leetcode.com/problems/convert-date-to-binary/">3280. Convert Date to Binary</a></h2><h3>Easy</h3><hr><div><p>You are given a string <code>date</code> representing a Gregorian calendar date in the <code>yyyy-mm-dd</code> format.</p>

<p><code>date</code> can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in <code>year-month-day</code> format.</p>

<p>Return the <strong>binary</strong> representation of <code>date</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">date = "2080-02-29"</span></p>

<p><strong>Output:</strong> <span class="example-io">"100000100000-10-11101"</span></p>

<p><strong>Explanation:</strong></p>

<p><span class="example-io">100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.</span></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">date = "1900-01-01"</span></p>

<p><strong>Output:</strong> <span class="example-io">"11101101100-1-1"</span></p>

<p><strong>Explanation:</strong></p>

<p><span class="example-io">11101101100, 1, and 1 are the binary representations of 1900, 1, and 1 respectively.</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>date.length == 10</code></li>
	<li><code>date[4] == date[7] == '-'</code>, and all other <code>date[i]</code>'s are digits.</li>
	<li>The input is generated such that <code>date</code> represents a valid Gregorian calendar date between Jan 1<sup>st</sup>, 1900 and Dec 31<sup>st</sup>, 2100 (both inclusive).</li>
</ul>
</div>