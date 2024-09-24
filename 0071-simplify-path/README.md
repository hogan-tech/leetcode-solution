<h2><a href="https://leetcode.com/problems/simplify-path/">71. Simplify Path</a></h2><h3>Medium</h3><hr><div><p>You are given an <em>absolute</em> path for a Unix-style file system, which always begins with a slash <code>'/'</code>. Your task is to transform this absolute path into its <strong>simplified canonical path</strong>.</p>

<p>The <em>rules</em> of a Unix-style file system are as follows:</p>

<ul>
	<li>A single period <code>'.'</code> represents the current directory.</li>
	<li>A double period <code>'..'</code> represents the previous/parent directory.</li>
	<li>Multiple consecutive slashes such as <code>'//'</code> and <code>'///'</code> are treated as a single slash <code>'/'</code>.</li>
	<li>Any sequence of periods that does <strong>not match</strong> the rules above should be treated as a <strong>valid directory or</strong> <strong>file </strong><strong>name</strong>. For example, <code>'...' </code>and <code>'....'</code> are valid directory or file names.</li>
</ul>

<p>The simplified canonical path should follow these <em>rules</em>:</p>

<ul>
	<li>The path must start with a single slash <code>'/'</code>.</li>
	<li>Directories within the path must be separated by exactly one slash <code>'/'</code>.</li>
	<li>The path must not end with a slash <code>'/'</code>, unless it is the root directory.</li>
	<li>The path must not have any single or double periods (<code>'.'</code> and <code>'..'</code>) used to denote current or parent directories.</li>
</ul>

<p>Return the <strong>simplified canonical path</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = "/home/"</span></p>

<p><strong>Output:</strong> <span class="example-io">"/home"</span></p>

<p><strong>Explanation:</strong></p>

<p>The trailing slash should be removed.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = "/home//foo/"</span></p>

<p><strong>Output:</strong> <span class="example-io">"/home/foo"</span></p>

<p><strong>Explanation:</strong></p>

<p>Multiple consecutive slashes are replaced by a single one.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = "/home/user/Documents/../Pictures"</span></p>

<p><strong>Output:</strong> <span class="example-io">"/home/user/Pictures"</span></p>

<p><strong>Explanation:</strong></p>

<p>A double period <code>".."</code> refers to the directory up a level (the parent directory).</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = "/../"</span></p>

<p><strong>Output:</strong> <span class="example-io">"/"</span></p>

<p><strong>Explanation:</strong></p>

<p>Going one level up from the root directory is not possible.</p>
</div>

<p><strong class="example">Example 5:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">path = "/.../a/../b/c/../d/./"</span></p>

<p><strong>Output:</strong> <span class="example-io">"/.../b/d"</span></p>

<p><strong>Explanation:</strong></p>

<p><code>"..."</code> is a valid name for a directory in this problem.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= path.length &lt;= 3000</code></li>
	<li><code>path</code> consists of English letters, digits, period <code>'.'</code>, slash <code>'/'</code> or <code>'_'</code>.</li>
	<li><code>path</code> is a valid absolute Unix path.</li>
</ul>
</div>