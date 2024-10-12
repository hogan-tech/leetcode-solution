<h2><a href="https://leetcode.com/problems/maximum-number-of-upgradable-servers/">3155. Maximum Number of Upgradable Servers</a></h2><h3>Medium</h3><hr><div><p>You have <code>n</code> data centers and need to upgrade their servers.</p>

<p>You are given four arrays <code>count</code>, <code>upgrade</code>, <code>sell</code>, and <code>money</code> of length <code>n</code>, which show:</p>

<ul>
	<li>The number of servers</li>
	<li>The cost of upgrading a single server</li>
	<li>The money you get by selling a server</li>
	<li>The money you initially have</li>
</ul>

<p>for each data center respectively.</p>

<p>Return an array <code>answer</code>, where for each data center, the corresponding element in <code>answer</code> represents the <strong>maximum</strong> number of servers that can be upgraded.</p>

<p>Note that the money from one data center <strong>cannot</strong> be used for another data center.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">count = [4,3], upgrade = [3,5], sell = [4,2], money = [8,9]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>For the first data center, if we sell one server, we'll have <code>8 + 4 = 12</code> units of money and we can upgrade the remaining 3 servers.</p>

<p>For the second data center, if we sell one server, we'll have <code>9 + 2 = 11</code> units of money and we can upgrade the remaining 2 servers.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">count = [1], upgrade = [2], sell = [1], money = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= count.length == upgrade.length == sell.length == money.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= count[i], upgrade[i], sell[i], money[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</div>