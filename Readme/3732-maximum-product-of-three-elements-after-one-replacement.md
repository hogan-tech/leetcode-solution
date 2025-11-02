<h2><a href="https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement">4101. Maximum Product of Three Elements After One Replacement</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>nums</code>.</p>

<p>You <strong>must</strong> replace <strong>exactly one</strong> element in the array with <strong>any</strong> integer value in the range <code>[-10<sup>5</sup>, 10<sup>5</sup>]</code> (inclusive).</p>

<p>After performing this single replacement, determine the <strong>maximum possible product</strong> of <strong>any three</strong> elements at <strong>distinct indices</strong> from the modified array.</p>

<p>Return an integer denoting the <strong>maximum product</strong> achievable.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-5,7,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">3500000</span></p>

<p><strong>Explanation:</strong></p>

<p>Replacing 0 with -10<sup>5</sup> gives the array <code>[-5, 7, -10<sup>5</sup>]</code>, which has a product <code>(-5) * 7 * (-10<sup>5</sup>) = 3500000</code>. The maximum product is 3500000.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-4,-2,-1,-3]</span></p>

<p><strong>Output:</strong> <span class="example-io">1200000</span></p>

<p><strong>Explanation:</strong></p>

<p>Two ways to achieve the maximum product include:</p>

<ul>
	<li><code>[-4, -2, -3]</code> &rarr; replace -2 with 10<sup>5</sup> &rarr; product = <code>(-4) * 10<sup>5</sup> * (-3) = 1200000</code>.</li>
	<li><code>[-4, -1, -3]</code> &rarr; replace -1 with 10<sup>5</sup> &rarr; product = <code>(-4) * 10<sup>5</sup> * (-3) = 1200000</code>.</li>
</ul>
The maximum product is 1200000.</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0,10,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no way to replace an element with another integer and not have a 0 in the array. Hence, the product of all three elements will always be 0, and the maximum product is 0.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
