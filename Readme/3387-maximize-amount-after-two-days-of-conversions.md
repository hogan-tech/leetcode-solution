<h2><a href="https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/">3387. Maximize Amount After Two Days of Conversions</a></h2><h3>Medium</h3><hr><div><p>You are given a string <code>initialCurrency</code>, and you start with <code>1.0</code> of <code>initialCurrency</code>.</p>

<p>You are also given four arrays with currency pairs (strings) and rates (real numbers):</p>

<ul>
	<li><code>pairs1[i] = [startCurrency<sub>i</sub>, targetCurrency<sub>i</sub>]</code> denotes that you can convert from <code>startCurrency<sub>i</sub></code> to <code>targetCurrency<sub>i</sub></code> at a rate of <code>rates1[i]</code> on <strong>day 1</strong>.</li>
	<li><code>pairs2[i] = [startCurrency<sub>i</sub>, targetCurrency<sub>i</sub>]</code> denotes that you can convert from <code>startCurrency<sub>i</sub></code> to <code>targetCurrency<sub>i</sub></code> at a rate of <code>rates2[i]</code> on <strong>day 2</strong>.</li>
	<li>Also, each <code>targetCurrency</code> can be converted back to its corresponding <code>startCurrency</code> at a rate of <code>1 / rate</code>.</li>
</ul>

<p>You can perform <strong>any</strong> number of conversions, <strong>including zero</strong>, using <code>rates1</code> on day 1, <strong>followed</strong> by any number of additional conversions, <strong>including zero</strong>, using <code>rates2</code> on day 2.</p>

<p>Return the <strong>maximum</strong> amount of <code>initialCurrency</code> you can have after performing any number of conversions on both days <strong>in order</strong>.</p>

<p><strong>Note: </strong>Conversion rates are valid, and there will be no contradictions in the rates for either day. The rates for the days are independent of each other.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0,3.0], pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]], rates2 = [4.0,5.0,6.0]</span></p>

<p><strong>Output:</strong> <span class="example-io">720.00000</span></p>

<p><strong>Explanation:</strong></p>

<p>To get the maximum amount of <strong>EUR</strong>, starting with 1.0 <strong>EUR</strong>:</p>

<ul>
	<li>On Day 1:
	<ul>
		<li>Convert <strong>EUR </strong>to <strong>USD</strong> to get 2.0 <strong>USD</strong>.</li>
		<li>Convert <strong>USD</strong> to <strong>JPY</strong> to get 6.0 <strong>JPY</strong>.</li>
	</ul>
	</li>
	<li>On Day 2:
	<ul>
		<li>Convert <strong>JPY</strong> to <strong>USD</strong> to get 24.0 <strong>USD</strong>.</li>
		<li>Convert <strong>USD</strong> to <strong>CHF</strong> to get 120.0 <strong>CHF</strong>.</li>
		<li>Finally, convert <strong>CHF</strong> to <strong>EUR</strong> to get 720.0 <strong>EUR</strong>.</li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">initialCurrency = "NGN", pairs1 = </span>[["NGN","EUR"]]<span class="example-io">, rates1 = </span>[9.0]<span class="example-io">, pairs2 = </span>[["NGN","EUR"]]<span class="example-io">, rates2 = </span>[6.0]</p>

<p><strong>Output:</strong> 1.50000</p>

<p><strong>Explanation:</strong></p>

<p>Converting <strong>NGN</strong> to <strong>EUR</strong> on day 1 and <strong>EUR</strong> to <strong>NGN</strong> using the inverse rate on day 2 gives the maximum amount.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"]], rates2 = [10.0]</span></p>

<p><strong>Output:</strong> <span class="example-io">1.00000</span></p>

<p><strong>Explanation:</strong></p>

<p>In this example, there is no need to make any conversions on either day.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= initialCurrency.length &lt;= 3</code></li>
	<li><code>initialCurrency</code> consists only of uppercase English letters.</li>
	<li><code>1 &lt;= n == pairs1.length &lt;= 10</code></li>
	<li><code>1 &lt;= m == pairs2.length &lt;= 10</code></li>
	<li><code>pairs1[i] == [startCurrency<sub>i</sub>, targetCurrency<sub>i</sub>]</code><!-- notionvc: c31b5bb8-4df6-4987-9bcd-6dff8a5f7cd4 --></li>
	<li><code>pairs2[i] == [startCurrency<sub>i</sub>, targetCurrency<sub>i</sub>]</code><!--{C}%3C!%2D%2D%20notionvc%3A%20c31b5bb8-4df6-4987-9bcd-6dff8a5f7cd4%20%2D%2D%3E--></li>
	<li><code>1 &lt;= startCurrency<sub>i</sub>.length, targetCurrency<sub>i</sub>.length &lt;= 3</code></li>
	<li><code>startCurrency<sub>i</sub></code> and <code>targetCurrency<sub>i</sub></code> consist only of uppercase English letters.</li>
	<li><code>rates1.length == n</code></li>
	<li><code>rates2.length == m</code></li>
	<li><code>1.0 &lt;= rates1[i], rates2[i] &lt;= 10.0</code></li>
	<li>The input is generated such that there are no contradictions or cycles in the conversion graphs for either day.</li>
</ul>
</div>