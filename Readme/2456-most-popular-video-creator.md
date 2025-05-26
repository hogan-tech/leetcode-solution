<h2><a href="https://leetcode.com/problems/most-popular-video-creator">2543. Most Popular Video Creator</a></h2><h3>Medium</h3><hr><p>You are given two string arrays <code>creators</code> and <code>ids</code>, and an integer array <code>views</code>, all of length <code>n</code>. The <code>i<sup>th</sup></code> video on a platform was created by <code>creators[i]</code>, has an id of <code>ids[i]</code>, and has <code>views[i]</code> views.</p>

<p>The <strong>popularity</strong> of a creator is the <strong>sum</strong> of the number of views on <strong>all</strong> of the creator&#39;s videos. Find the creator with the <strong>highest</strong> popularity and the id of their <strong>most</strong> viewed video.</p>

<ul>
	<li>If multiple creators have the highest popularity, find all of them.</li>
	<li>If multiple videos have the highest view count for a creator, find the lexicographically <strong>smallest</strong> id.</li>
</ul>

<p>Note: It is possible for different videos to have the same <code>id</code>, meaning that <code>id</code>s do not uniquely identify a video. For example, two videos with the same ID are considered as distinct videos with their own viewcount.</p>

<p>Return<em> </em>a <strong>2D array</strong> of <strong>strings</strong> <code>answer</code> where <code>answer[i] = [creators<sub>i</sub>, id<sub>i</sub>]</code> means that <code>creators<sub>i</sub></code> has the <strong>highest</strong> popularity and <code>id<sub>i</sub></code> is the <strong>id</strong> of their most <strong>popular</strong> video. The answer can be returned in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">creators = [&quot;alice&quot;,&quot;bob&quot;,&quot;alice&quot;,&quot;chris&quot;], ids = [&quot;one&quot;,&quot;two&quot;,&quot;three&quot;,&quot;four&quot;], views = [5,10,5,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;alice&quot;,&quot;one&quot;],[&quot;bob&quot;,&quot;two&quot;]]</span></p>

<p><strong>Explanation:</strong></p>

<p>The popularity of alice is 5 + 5 = 10.<br />
The popularity of bob is 10.<br />
The popularity of chris is 4.<br />
alice and bob are the most popular creators.<br />
For bob, the video with the highest view count is &quot;two&quot;.<br />
For alice, the videos with the highest view count are &quot;one&quot; and &quot;three&quot;. Since &quot;one&quot; is lexicographically smaller than &quot;three&quot;, it is included in the answer.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">creators = [&quot;alice&quot;,&quot;alice&quot;,&quot;alice&quot;], ids = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;], views = [1,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[&quot;alice&quot;,&quot;b&quot;]]</span></p>

<p><strong>Explanation:</strong></p>

<p>The videos with id &quot;b&quot; and &quot;c&quot; have the highest view count.<br />
Since &quot;b&quot; is lexicographically smaller than &quot;c&quot;, it is included in the answer.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == creators.length == ids.length == views.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= creators[i].length, ids[i].length &lt;= 5</code></li>
	<li><code>creators[i]</code> and <code>ids[i]</code> consist only of lowercase English letters.</li>
	<li><code>0 &lt;= views[i] &lt;= 10<sup>5</sup></code></li>
</ul>
