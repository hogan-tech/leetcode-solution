<h2> 1677 106
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold</h2><hr><div><p>Given an array of integers <code>arr</code> and two integers <code>k</code> and <code>threshold</code>, return <em>the number of sub-arrays of size </em><code>k</code><em> and average greater than or equal to </em><code>threshold</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
<strong>Output:</strong> 6
<strong>Explanation:</strong> The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= arr.length</code></li>
	<li><code>0 &lt;= threshold &lt;= 10<sup>4</sup></code></li>
</ul>
</div>