<h2> 67 93
2408. Design SQL</h2><hr><div><p>You are given two string arrays, <code>names</code> and <code>columns</code>, both of size <code>n</code>. The <code>i<sup>th</sup></code> table is represented by the name <code>names[i]</code> and contains <code>columns[i]</code> number of columns.</p>

<p>You need to implement a class that supports the following <strong>operations</strong>:</p>

<ul>
	<li><strong>Insert</strong> a row in a specific table with an id assigned using an <em>auto-increment</em> method, where the id of the first inserted row is 1, and the id of each <em>new </em>row inserted into the same table is <strong>one greater</strong> than the id of the <strong>last inserted</strong> row, even if the last row was <em>removed</em>.</li>
	<li><strong>Remove</strong> a row from a specific table. Removing a row <strong>does not</strong> affect the id of the next inserted row.</li>
	<li><strong>Select</strong> a specific cell from any table and return its value.</li>
	<li><strong>Export</strong> all rows from any table in csv format.</li>
</ul>

<p>Implement the <code>SQL</code> class:</p>

<ul>
	<li><code>SQL(String[] names, int[] columns)</code>

	<ul>
		<li>Creates the <code>n</code> tables.</li>
	</ul>
	</li>
	<li><code>bool ins(String name, String[] row)</code>
	<ul>
		<li>Inserts <code>row</code> into the table <code>name</code> and returns <code>true</code>.</li>
		<li>If <code>row.length</code> <strong>does not</strong> match the expected number of columns, or <code>name</code> is <strong>not</strong> a valid table, returns <code>false</code> without any insertion.</li>
	</ul>
	</li>
	<li><code>void rmv(String name, int rowId)</code>
	<ul>
		<li>Removes the row <code>rowId</code> from the table <code>name</code>.</li>
		<li>If <code>name</code> is <strong>not</strong> a valid table or there is no row with id <code>rowId</code>, no removal is performed.</li>
	</ul>
	</li>
	<li><code>String sel(String name, int rowId, int columnId)</code>
	<ul>
		<li>Returns the value of the cell at the specified <code>rowId</code> and <code>columnId</code> in the table <code>name</code>.</li>
		<li>If <code>name</code> is <strong>not</strong> a valid table, or the cell <code>(rowId, columnId)</code> is <strong>invalid</strong>, returns <code>"&lt;null&gt;"</code>.</li>
	</ul>
	</li>
	<li><code>String[] exp(String name)</code>
	<ul>
		<li>Returns the rows present in the table <code>name</code>.</li>
		<li>If name is <strong>not</strong> a valid table, returns an empty array. Each row is represented as a string, with each cell value (<strong>including</strong> the row's id) separated by a <code>","</code>.</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<pre class="example-io">["SQL","ins","sel","ins","exp","rmv","sel","exp"]
[[["one","two","three"],[2,3,1]],["two",["first","second","third"]],["two",1,3],["two",["fourth","fifth","sixth"]],["two"],["two",1],["two",2,2],["two"]]
</pre>

<p><strong>Output:</strong></p>

<pre class="example-io">[null,true,"third",true,["1,first,second,third","2,fourth,fifth,sixth"],null,"fifth",["2,fourth,fifth,sixth"]]</pre>

<p><strong>Explanation:</strong></p>

<pre class="example-io">// Creates three tables.
SQL sql = new SQL(["one", "two", "three"], [2, 3, 1]);

// Adds a row to the table "two" with id 1. Returns True.
sql.ins("two", ["first", "second", "third"]);

// Returns the value "third" from the third column
// in the row with id 1 of the table "two".
sql.sel("two", 1, 3);

// Adds another row to the table "two" with id 2. Returns True.
sql.ins("two", ["fourth", "fifth", "sixth"]);

// Exports the rows of the table "two".
// Currently, the table has 2 rows with ids 1 and 2.
sql.exp("two");

// Removes the first row of the table "two". Note that the second row
// will still have the id 2.
sql.rmv("two", 1);

// Returns the value "fifth" from the second column
// in the row with id 2 of the table "two".
sql.sel("two", 2, 2);

// Exports the rows of the table "two".
// Currently, the table has 1 row with id 2.
sql.exp("two");
</pre>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<pre class="example-io">["SQL","ins","sel","rmv","sel","ins","ins"]
[[["one","two","three"],[2,3,1]],["two",["first","second","third"]],["two",1,3],["two",1],["two",1,2],["two",["fourth","fifth"]],["two",["fourth","fifth","sixth"]]]
</pre>

<p><strong>Output:</strong></p>

<pre class="example-io">[null,true,"third",null,"&lt;null&gt;",false,true]
</pre>

<p><strong>Explanation:</strong></p>

<pre class="example-io">// Creates three tables.
SQL sQL = new SQL(["one", "two", "three"], [2, 3, 1]); 

// Adds a row to the table "two" with id 1. Returns True. 
sQL.ins("two", ["first", "second", "third"]); 

// Returns the value "third" from the third column 
// in the row with id 1 of the table "two".
sQL.sel("two", 1, 3); 

// Removes the first row of the table "two".
sQL.rmv("two", 1); 

// Returns "&lt;null&gt;" as the cell with id 1 
// has been removed from table "two".
sQL.sel("two", 1, 2); 

// Returns False as number of columns are not correct.
sQL.ins("two", ["fourth", "fifth"]); 

// Adds a row to the table "two" with id 2. Returns True.
sQL.ins("two", ["fourth", "fifth", "sixth"]); 
</pre>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == names.length == columns.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= names[i].length, row[i].length, name.length &lt;= 10</code></li>
	<li><code>names[i]</code>, <code>row[i]</code>, and <code>name</code> consist only of lowercase English letters.</li>
	<li><code>1 &lt;= columns[i] &lt;= 10</code></li>
	<li><code>1 &lt;= row.length &lt;= 10</code></li>
	<li>All <code>names[i]</code> are <strong>distinct</strong>.</li>
	<li>At most <code>2000</code> calls will be made to <code>ins</code> and <code>rmv</code>.</li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>sel</code>.</li>
	<li>At most <code>500</code> calls will be made to <code>exp</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:</strong> Which approach would you choose if the table might become sparse due to many deletions, and why? Consider the impact on memory usage and performance.</div>