<h2><a href="https://leetcode.com/problems/calculate-score-after-performing-instructions">3732. Calculate Score After Performing Instructions</a></h2><h3>Medium</h3><hr><p>You are given two arrays, <code>instructions</code> and <code>values</code>, both of size <code>n</code>.</p>

<p>You need to simulate a process based on the following rules:</p>

<ul>
	<li>You start at the first instruction at index <code>i = 0</code> with an initial score of 0.</li>
	<li>If <code>instructions[i]</code> is <code>&quot;add&quot;</code>:
	<ul>
		<li>Add <code>values[i]</code> to your score.</li>
		<li>Move to the next instruction <code>(i + 1)</code>.</li>
	</ul>
	</li>
	<li>If <code>instructions[i]</code> is <code>&quot;jump&quot;</code>:
	<ul>
		<li>Move to the instruction at index <code>(i + values[i])</code> without modifying your score.</li>
	</ul>
	</li>
</ul>

<p>The process ends when you either:</p>

<ul>
	<li>Go out of bounds (i.e., <code>i &lt; 0 or i &gt;= n</code>), or</li>
	<li>Attempt to revisit an instruction that has been previously executed. The revisited instruction is not executed.</li>
</ul>

<p>Return your score at the end of the process.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">instructions = [&quot;jump&quot;,&quot;add&quot;,&quot;add&quot;,&quot;jump&quot;,&quot;add&quot;,&quot;jump&quot;], values = [2,1,3,1,-2,-3]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Simulate the process starting at instruction 0:</p>

<ul>
	<li>At index 0: Instruction is <code>&quot;jump&quot;</code>, move to index <code>0 + 2 = 2</code>.</li>
	<li>At index 2: Instruction is <code>&quot;add&quot;</code>, add <code>values[2] = 3</code> to your score and move to index 3. Your score becomes 3.</li>
	<li>At index 3: Instruction is <code>&quot;jump&quot;</code>, move to index <code>3 + 1 = 4</code>.</li>
	<li>At index 4: Instruction is <code>&quot;add&quot;</code>, add <code>values[4] = -2</code> to your score and move to index 5. Your score becomes 1.</li>
	<li>At index 5: Instruction is <code>&quot;jump&quot;</code>, move to index <code>5 + (-3) = 2</code>.</li>
	<li>At index 2: Already visited. The process ends.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">instructions = [&quot;jump&quot;,&quot;add&quot;,&quot;add&quot;], values = [3,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>Simulate the process starting at instruction 0:</p>

<ul>
	<li>At index 0: Instruction is <code>&quot;jump&quot;</code>, move to index <code>0 + 3 = 3</code>.</li>
	<li>At index 3: Out of bounds. The process ends.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">instructions = [&quot;jump&quot;], values = [0]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>Simulate the process starting at instruction 0:</p>

<ul>
	<li>At index 0: Instruction is <code>&quot;jump&quot;</code>, move to index <code>0 + 0 = 0</code>.</li>
	<li>At index 0: Already visited. The process ends.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == instructions.length == values.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>instructions[i]</code> is either <code>&quot;add&quot;</code> or <code>&quot;jump&quot;</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= values[i] &lt;= 10<sup>5</sup></code></li>
</ul>
